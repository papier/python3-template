"""Start the application."""
import os
import signal
import types
import typing


def main() -> None:
    """Install signal handlers and start the application."""
    run_flag: bool = True
    received_signum: typing.Optional[signal.Signals] = None

    def create_signal_handler(
        signum_to_handle: signal.Signals,
    ) -> typing.Union[
        typing.Callable[[int, typing.Optional[signal.FrameType]], typing.Any],
        int,
        signal.Handlers,
        None,
    ]:
        def handler(
            signum: signal.Signals, frame: typing.Optional[types.FrameType]
        ) -> typing.Any:
            nonlocal run_flag
            nonlocal received_signum
            if run_flag:
                run_flag = False
                received_signum = signum_to_handle

        return handler

    signal.signal(signal.SIGINT, create_signal_handler(signal.SIGINT))
    signal.signal(signal.SIGTERM, create_signal_handler(signal.SIGTERM))

    print(f"Press Ctrl-C or send SIGTERM to {os.getpid()}")
    while run_flag:
        pass

    if received_signum is not None:
        # Restore default signal handler
        signal.signal(received_signum, signal.SIG_DFL)
        # Resend the signal to this process
        os.kill(os.getpid(), received_signum)


if __name__ == "__main__":
    main()
