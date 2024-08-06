# pythonanywhere-flask

## Deploying to Pythonanywhere

1. Sign up for a [pythonanywhere](https://www.pythonanywhere.com) account (or login if you already have one).
2. Go to the Web menu item and then press the Add new web app button.
3. Click Next, then click on Flask and click on the latest version of Python that you see there. Then click Next again to accept the project path.
4. In the Code section of the Web menu page click on Go to Directory next to Source Code.
5. Click "Open Bash console here" at top of page.
6. Replaced the content of mysite with this repo:

    ```bash
    git clone https://github.com/johneastman/pythonanywhere-flask.git mysite
    ```

    - You may need to delete or rename the existing mysite directory:

        ```bash
        # delete
        rm -rf mysite

        # rename
        mv mysite/ mysite2/
        ```

7. Make sure the last line of `*wsgi.py` is this:
    ```python
    from app import app as flask
    ```
8. Back on the dashboard, click "Web" and then click `Reload <domain name>`
