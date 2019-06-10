# auto-speedtest with Google Spreadsheet

Check-up your connection and upload speedtest stats inside Google Spreadsheet
![sheet](https://lh5.googleusercontent.com/cCXT1FPoxUJxQEScxJH8jYFhVs3uuS_6cIJv6ETwLnursai38ItlksQpHy69pqdzLFMcIjghBa3wiw=w1842-h998-rw)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for testing purposes. See installing notes for how to deploy the project on a live system.

### Prerequisites

* [speedtest-cli](https://github.com/sivel/speedtest-cli) API for Python 
* [Google API](https://developers.google.com/api-client-library/python/start/installation) for Python
* *client_secret.json*
* [oauth2client](https://github.com/google/oauth2client) for Python
* ID of your spreedsheet already created

### Installing

Modify auto-speedtest.py :
```
line 30 : spreadsheetId = 'your sheet id'
```
How to get spreadsheetId ? 



Installing For Linux sytem : 
```
sudo python -m pip install --upgrade pip oauth2client
sudo python -m pip install --upgrade pip google-api-python-client
sudo python -m pip install --upgrade pip speedtest-cli
```
if you use only ssh :
You can't open browser, Python show an URL. Copy and paste to your remote computer to connected with your google account for get a password asked by Python

Place auto-speedtest.py and client_secret.json([see also](https://developers.google.com/api-client-library/python/guide/aaa_client_secrets)) inside the same folder. Run .py with IDE or Python Interpreter.
Using every *t* time with [crontab](https://en.wikipedia.org/wiki/Cron) on linux system (Raspberry Pi) 

## Built With

* [Thonny](http://thonny.org/) - IDE for Python

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **William Colpaert** - *Initial work* - [KaoruKanon](https://gist.github.com/KaoruKanon/)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
