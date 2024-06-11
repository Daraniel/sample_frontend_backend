from app import create_app

app = create_app()

if __name__ == '__main__':
    # used only when running the app directly, on production it should be used with the flask command,
    # which also allows setting the host and port (or alternatively pass the host and port to the run `function`)
    app.run()
