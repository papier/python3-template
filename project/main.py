"""Start the application."""
import os
import signal


def main():
    """Install signal handlers and start the application."""
    run_flag = True
    received_signal = None

    def create_signal_handler(handled_signal):
        def handler(signal, frame):
            nonlocal run_flag
            nonlocal received_signal
            if run_flag:
                run_flag = False
                received_signal = handled_signal

        return handler

    signal.signal(signal.SIGINT, create_signal_handler(signal.SIGINT))
    signal.signal(signal.SIGTERM, create_signal_handler(signal.SIGTERM))

    print(f"Press Ctrl-C or send SIGTERM to {os.getpid()}")
    while run_flag:
        pass

    if received_signal is not None:
        # Restore default signal handler
        signal.signal(received_signal, signal.SIG_DFL)
        # Resend the signal to this process
        os.kill(os.getpid(), received_signal)


if __name__ == "__main__":
    main()
