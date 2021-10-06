import inspect
import copy


class Testconfig:
    gmail = {
        "primaryServer": {
            "server": "",
            "uid": "",
            "pw": "",
            "port": 0,
            "sender": "",
            "encryption": 0,  # 0: None, 1: SSL/TLS, 2: STARTTLS
        },
        "secondaryServer": {
            "server": "smtp.gmail.com",
            "uid": "kodico.wiznet2020@gmail.com",
            "pw": "0vud0v1!",
            "port": 587,
            # "sender": "kodico.wiznet2020@gmail.com",
            "encryption": 2,  # 0: None, 1: SSL/TLS, 2: STARTTLS,'sender': 'kodico.wiznet2020@gmail.com'
        },
        "msg": {
            "receiver": "kung@kodico.co.kr, joseph@wiznet.io",
            "subject": "test from 630s",
            "content": "this is test from 630s",
        },
    }


class Testlist:
    def __init__(self) -> None:
        self.smtp_wait_list = []
        self.config = None

    def setConfig(
        self, server=None, receiver=None, subject=None, content=None, files=None
    ):
        if server:
            print(f"current ={self.config}")
            print(f"incoming={server}")
            self.config = server
        if receiver:
            self.config["msg"]["receiver"] = receiver
        if subject:
            self.config["msg"]["subject"] = subject
        if content:
            self.config["msg"]["content"] = content
        self.config["files"] = files

    def send(self):
        self.smtp_wait_list.append(copy.deepcopy(self.config))
        print(
            f"************ caller:{inspect.stack()[1][3]} config:{self.config} list are {self.smtp_wait_list} ****************"
        )


test = Testlist()
test.setConfig(
    server={
        "primaryServer": {
            "server": "",
            "uid": "",
            "pw": "",
            "port": 0,
            "sender": "",  # 0: None, 1: SSL/TLS, 2: STARTTLS
            "encryption": 0,
        },
        "secondaryServer": {
            "server": "smtp.gmail.com",
            "uid": "kodico.wiznet2020@gmail.com",
            "pw": "0vud0v1!",
            "port": 587,  # "sender": "kodico.wiznet2020@gmail.com",
            # 0: None, 1: SSL/TLS, 2: STARTTLS,'sender': 'kodico.wiznet2020@gmail.com'
            "encryption": 2,
        },
        "msg": {
            "receiver": "kung@kodico.co.kr, joseph@wiznet.io",
            "subject": "test from 630s",
            "content": "this is test from 630s",
        },
    }
)
test.send()
test.setConfig(subject="hihi")
test.send()
