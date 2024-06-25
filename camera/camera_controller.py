# Copyright (C) 2023 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

from PySide6.QtCore import QBuffer, QByteArray, QThread, QTimer, Slot
from PySide6.QtGui import QImage
from PySide6.QtMultimedia import (
    QCamera,
    QCameraDevice,
    QImageCapture,
    QMediaCaptureSession,
    QMediaDevices,
)
from PySide6.QtWidgets import QMainWindow, QMessageBox

import cnn_model

from .camera_view import Ui_Camera
from .stopwatch import StopWatch


class Camera(QMainWindow):
    def __init__(self):
        super().__init__()

        self.m_camera: QCamera = None
        self.m_imageCapture: QImageCapture = None
        self.m_captureSession = QMediaCaptureSession()

        self._ui = Ui_Camera()
        self._ui.setupUi(self)

        # Inicializar la camara con el dispositivo por defecto
        self.setCamera(QMediaDevices.defaultVideoInput())

        # Inicializa el temporizador para analizar una captura de la imagen
        self.initStopWatch()

    def setCamera(self, cameraDevice: QCameraDevice):
        self.m_camera = QCamera(cameraDevice)
        self.m_captureSession.setCamera(self.m_camera)

        self.m_camera.errorOccurred.connect(self.displayCameraError)

        self.m_imageCapture = QImageCapture()
        self.m_captureSession.setImageCapture(self.m_imageCapture)
        self.m_imageCapture.imageCaptured.connect(self.processCapturedImage)
        self.m_imageCapture.errorOccurred.connect(self.displayCaptureError)

        self.m_captureSession.setVideoOutput(self._ui.viewfinder)

        self.m_camera.start()

    def initStopWatch(self):
        self.cnn_worker = QThread()
        self.stopwatch = StopWatch()

        # Mueve el temporizador a un hilo diferente
        self.stopwatch.moveToThread(self.cnn_worker)

        # Conecta las señales apropiadas para usar el temporizador y tomar la captura
        self.cnn_worker.started.connect(self.stopwatch.start_timer)
        self.stopwatch.update_signal.connect(self.take_screenshoot)

        # Inicia el hilo de ejecución
        self.cnn_worker.start()

    def take_screenshoot(self):
        # Indicarle al control QImageCapture que realice la captura
        # Esto disparará "processCapturedImage" automáticamente
        #  con los parámetros necesarios
        self.m_imageCapture.capture()

    @Slot(int, QImageCapture.Error, str)
    def displayCaptureError(self, id, error, errorString):
        QMessageBox.warning(self, "Image Capture Error", errorString)

    @Slot()
    def displayCameraError(self):
        if self.m_camera.error() != QCamera.NoError:
            QMessageBox.warning(self, "Camera Error", self.m_camera.errorString())

    @Slot(int, QImage)
    def processCapturedImage(self, requestId, img: QImage):
        # Definir un buffer especial de QT para datos binarios
        img_bytes = QByteArray()
        img_buffer = QBuffer(img_bytes)
        img_buffer.open(QBuffer.WriteOnly)

        # Guardar los datos de la imagen en el buffer
        img.save(img_buffer, "JPG")

        # Detectar el tipo de gesto
        gesture = cnn_model.detect_gesture(img_bytes.data())

        # Establecer el texto con el gesto obtenido
        self._ui.label_category.setText(f"Gesto: {gesture}")

    def release_resources(self):
        self.stopwatch.stop_signal.emit()
        self.cnn_worker.quit()
        self.cnn_worker.wait()
