# mitm-demo

## python3 + selenium + chromedrive + mitmproxy

### Initializing environment:

You should already have the `Chrome` browser.

install [python3](https://www.python.org/downloads/)

download [chromedrive](https://chromedriver.chromium.org/downloads) and unzip, then copy the file to `C:\Windows\System32`

install python module:

```powershell
pip install selenium
pip install mitmproxy
pip install requests
```
Note that in Windows operating systems, if `mitmproxy` fails to install, you may need to install [Visual C++ runtime](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads)


### After installation, the console launches the command:

```powershell
 mitmweb -s .\my-addon.py
```

### Another console to run the command:

```powershell
 python j-6000.py
```

### That's all.
