from PySide6.QtCore import QObject, QTimer, Signal


# Temporizador de Qt para ejecutarse en un hilo por separado
class StopWatch(QObject):
    # Señal para comunicarse con el hilo principal
    update_signal = Signal()
    stop_signal = Signal()

    def __init__(self):
        super().__init__()

    def start_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.watch)
        self.stop_signal.connect(self.stop_timer)

        # Crea un temporizador de 4 segundos (4000 ms)
        self.timer.start(4000)

    def stop_timer(self):
        self.timer.stop()

    def watch(self):
        self.update_signal.emit()
