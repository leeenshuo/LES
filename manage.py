import json
import os

DATA_FILE = 'participants.json'

class Participant:
    def __init__(self, pid, name):
        self.pid = pid
        self.name = name
        self.arrived = False
        self.paid = False
        self.return_confirmed = False

    def to_dict(self):
        return {
            'pid': self.pid,
            'name': self.name,
            'arrived': self.arrived,
            'paid': self.paid,
            'return_confirmed': self.return_confirmed,
        }

    @classmethod
    def from_dict(cls, data):
        p = cls(data['pid'], data['name'])
        p.arrived = data.get('arrived', False)
        p.paid = data.get('paid', False)
        p.return_confirmed = data.get('return_confirmed', False)
        return p


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Participant.from_dict(d) for d in data]
    return []


def save_data(participants):
    data = [p.to_dict() for p in participants]
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def find_participant(participants, pid):
    for p in participants:
        if p.pid == pid:
            return p
    return None


def add_participant(participants):
    pid = input('请输入ID: ')
    name = input('请输入姓名: ')
    if find_participant(participants, pid):
        print('该ID已经存在!')
        return
    p = Participant(pid, name)
    participants.append(p)
    print('添加成功!')


def list_participants(participants):
    for p in participants:
        print(f"ID: {p.pid}, 姓名: {p.name}, 到场: {p.arrived}, 缴费: {p.paid}, 回程确认: {p.return_confirmed}")


def check_in(participants):
    pid = input('请输入要签到的ID: ')
    p = find_participant(participants, pid)
    if p:
        p.arrived = True
        print('签到完成!')
    else:
        print('未找到该参加者')


def mark_paid(participants):
    pid = input('请输入已缴费的ID: ')
    p = find_participant(participants, pid)
    if p:
        p.paid = True
        print('记录缴费成功!')
    else:
        print('未找到该参加者')


def confirm_return(participants):
    pid = input('请输入确认回程的ID: ')
    p = find_participant(participants, pid)
    if p:
        p.return_confirmed = True
        print('回程确认成功!')
    else:
        print('未找到该参加者')


def main_menu(participants):
    while True:
        print('\n菜单:')
        print('1. 添加参加者')
        print('2. 列出参加者')
        print('3. 签到')
        print('4. 记录缴费')
        print('5. 确认回程')
        print('6. 保存并退出')
        choice = input('请选择操作: ')
        if choice == '1':
            add_participant(participants)
        elif choice == '2':
            list_participants(participants)
        elif choice == '3':
            check_in(participants)
        elif choice == '4':
            mark_paid(participants)
        elif choice == '5':
            confirm_return(participants)
        elif choice == '6':
            save_data(participants)
            print('数据已保存, 退出程序')
            break
        else:
            print('无效的选择')


if __name__ == '__main__':
    participants = load_data()
    main_menu(participants)
