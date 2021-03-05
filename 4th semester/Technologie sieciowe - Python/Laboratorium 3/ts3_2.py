import random
import os
import math
import time


KOLIZJA = "k"


class Signal():
    def __init__(self, status, data):
        # status - sygnał idący w prawo/ w lewo
        self.status = status
        self.data = data
    

class PC():
    def __init__(self, username, data, interval, location):
        self.username = username
        # 0 - nasłuchuje, 1 - wysyła
        self.status = 0
        self.data = data
        self.interval = interval
        self.location = location
        self.pause = interval
        self.received_data = []
        self.max_distance = 0
        self.actual_time = 0
        self.collision_counter = 0
        self.last_signal = ''

    def action(self, signals):
        # return: 0 - nasłuchuj, 1 - nadawaj, 2 - zgłoś kolizję
        # jeżeli jest tylko jeden sygnał, to chcemy go obsłużyć
        if len(signals) == 1:
            if signals[0].data == KOLIZJA:
                self.last_signal = ''
            elif signals[0].data != self.last_signal and self.last_signal != '':
                self.received_data.append(self.last_signal)
                self.last_signal = signals[0].data
            else:
                self.last_signal = signals[0].data
        
        #jeżeli sygnał przestał być nadawany i nie ma nowych, to zapisujemy nowe dane
        elif len(signals) == 0:
            if self.last_signal != '':
                self.received_data.append(self.last_signal)
                self.last_signal = ''

        # więcej niż jeden sygnał na raz - kolizja
        else:
            self.last_signal = ''

        # nasłuchujemy
        if self.pause > 0 and self.status == 0:
            self.pause -= 1

        if self.pause > 0 and self.status == 0:
            return 0

        if self.status == 0 and len(signals) > 0:
            return 0
            
        # jeżeli nic nie otrzymujemy, a pauza = 0, to chcemy wysłać sygnał
        if self.pause == 0 and self.status == 0:
            self.status = 1
            return 1
        
        # w trakcie wysyłania
        if self.status == 1 and len(signals) == 0:
            self.actual_time += 1

            #czy na penwo nie było kolizji - odległość do dalszego brzegu i z powrotem
            if self.actual_time == self.max_distance * 2:
                #print(self.username, "rozeslal swoje dane")
                self.status = 0
                self.actual_time = 0
                self.pause = self.interval
                self.collision_counter = 0
                return 0
            else:

                # nie wiemy czy na pewno nie było kolizji, więc dalej wysyłamy te dane
                return 1

        # jeżeli w trakcie wysyłania danych odbierzemy inne dane, to zaznaczamy kolizję
        if self.status == 1 and len(signals) > 0 and signals[0] != KOLIZJA:
            self.status = 0
            self.actual_time = 0
            self.collision_counter += 1
            return 2


class Network():
    def __init__(self, length, computers):
        self.signals = [[] for i in range(length)]
        self.computers = computers
        self.length = length
        self.time = 0
        self.end = False

        for pc in computers:
            pc.max_distance = max(pc.location, length - pc.location - 1)

    def action(self):
        self.time += 1

        #przesuwanie sygnałów do kolejnych węzłów
        signals_tmp = [[] for i in range (self.length)]
        for i in range(self.length):
            for signal in self.signals[i]:
                if signal.status == "left" and i > 0:
                    signals_tmp[i - 1].append(signal)
                if signal.status == "right" and i + 1 < self.length:
                    signals_tmp[i + 1].append(signal)
                if signal.status == "self":
                    signal.status = "none"
                    signals_tmp[i].append(signal)
        self.signals = signals_tmp

        #print("czas: ", self.time)
        for i in range(len(self.signals)):
            #print('|', end='')
            #for u in self.computers:
                #if u.location == i: 
                    #print(u.username, ":", end='')
            if len(self.signals[i]) > 1:
                print('!', end='')
                '''for s in self.signals[i]:
                    print(s.data, end='')'''
            if len(self.signals[i]) == 1:
                print(self.signals[i][0].data, end='')
            elif len(self.signals[i]) == 0:
                print(end=' ')
        #print('|', end='')
        print()
        '''for u in self.computers:
            print(u.username, ": odebrane: ", u.received_data, " ostani sygnał: ", u.last_signal)'''
        #print("_"*100)

        signals_tmp = [[] for i in range (self.length)]
        for i in range(self.length):
            for signal in self.signals[i]:
                if signal.status != "none":
                    signals_tmp[i].append(signal)
        self.signals = signals_tmp

        for user in self.computers:
            action = user.action(self.signals[user.location])
            if action == 1:
                self.signals[user.location].append(Signal("left", user.data))
                self.signals[user.location].append(Signal("right", user.data))
                self.signals[user.location].append(Signal("self", user.data))
            if action == 2:
                user.pause = random.randint(1, (2**(min(user.collision_counter, 10)) - 1)*self.length)
                if user.collision_counter >= 15:
                    self.end = True
                self.signals[user.location].append(Signal("left", KOLIZJA))
                self.signals[user.location].append(Signal("right", KOLIZJA))


def main():
    pc1 = PC("A", "a", 3, 0)
    pc2 = PC("B", "b", 16, 10)
    pc3 = PC("C", "c", 7, 19)
    siec = Network(60, [pc1, pc2, pc3])
    while not siec.end:
        #os.system("clear")
        siec.action()
        time.sleep(1)


if __name__ == "__main__":
    main()