
import tkinter

root = tkinter.Tk()
root.minsize(360,680)

class FError(Exception):
    pass


class MyCalculator():

    def __init__(self, width, height, title):

        root.minsize(height=height, width=width)
        root.maxsize(height=height, width=width)
        root.title(title)

        self.nums = 1
        self.top_frame = None
        self.calList = []
        self.flag = False

        self.result = 0
        self.result_panel1 = None
        self.result_panel2 = None

        self.format = True


    def set_label(self):
        self.top_frame = tkinter.Frame(root,width=360,height=200)
        self.top_frame.place(x=0,y=0)

        self.result_panel1 = tkinter.StringVar()
        self.result_panel1.set('')
        self.result_panel2 = tkinter.StringVar()
        self.result_panel2.set(0)

        result_label1 = tkinter.Label(self.top_frame, font=('微软雅黑', 25), bg='#FFFEFF', bd='9', fg='#000000', anchor='se',
                              textvariable=self.result_panel1)
        result_label1.place(width=360, height=100)
        result_label2 = tkinter.Label(self.top_frame,font=('微软雅黑', 30), bg='#FFFEFF', bd='9', fg='#000000', anchor='se',
                               textvariable=self.result_panel2)
        result_label2.place(x=0,y=100, width=360, height=100)


    def set_span(self):

        self.bootom_frame = tkinter.Frame(root, width=360, height=480)

        self.bootom_frame.place(x=0, y=200)

        button_c = tkinter.Button(self.bootom_frame, text='Clear', bd='0', font=('微软雅黑', 20), bg='#69B3AD',
                                  fg='#FFFEFF', command=lambda: self.pressC())
        button_c.place(x=0, y=0, width=90, height=96)

        button_back = tkinter.Button(self.bootom_frame, text='Delete', bd='0', font=('微软雅黑', 20), bg='#69B3AD',
                                     fg='#FFFEFF', command=lambda: self.pressBack())
        button_back.place(x=90, y=0, width=90, height=96)

        button_left = tkinter.Button(self.bootom_frame, text='(', bd='0', font=('微软雅黑', 20), bg='#69B3AD',
                                     fg='#FFFEFF', command=lambda: self.pressLeft())
        button_left.place(x=180, y=0, width=90, height=96)

        button_right = tkinter.Button(self.bootom_frame, text=')', bd='0', font=('微软雅黑', 20), bg='#69B3AD',
                                      fg='#FFFEFF', command=lambda: self.pressRight())
        button_right.place(x=270, y=0, width=90, height=96)

        button_1 = tkinter.Button(self.bootom_frame, text='1', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('1'))
        button_1.place(x=0, y=96, width=90, height=96)

        button_2 = tkinter.Button(self.bootom_frame, text='2', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('2'))
        button_2.place(x=90, y=96, width=90, height=96)

        button_3 = tkinter.Button(self.bootom_frame, text='3', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('3'))
        button_3.place(x=180, y=96, width=90, height=96)

        button_plus = tkinter.Button(self.bootom_frame, text='+', bd='0', font=('微软雅黑', 20), bg='#69B3AD',
                                     fg='#FFFEFF', command=lambda: self.pressOperation('+'))
        button_plus.place(x=270, y=96, width=90, height=96)

        button_4 = tkinter.Button(self.bootom_frame, text='4', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('4'))
        button_4.place(x=0, y=192, width=90, height=96)

        button_5 = tkinter.Button(self.bootom_frame, text='5', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('5'))
        button_5.place(x=90, y=192, width=90, height=96)

        button_6 = tkinter.Button(self.bootom_frame, text='6', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('6'))
        button_6.place(x=180, y=192, width=90, height=96)

        button_sub = tkinter.Button(self.bootom_frame, text='-', bd='0', font=('微软雅黑', 20), bg='#69B3AD',
                                    fg='#FFFEFF', command=lambda: self.pressOperation('-'))
        button_sub.place(x=270, y=192, width=90, height=96)

        button_7 = tkinter.Button(self.bootom_frame, text='7', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('7'))
        button_7.place(x=0, y=288, width=90, height=96)

        button_8 = tkinter.Button(self.bootom_frame, text='8', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('8'))
        button_8.place(x=90, y=288, width=90, height=96)

        button_9 = tkinter.Button(self.bootom_frame, text='9', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('9'))
        button_9.place(x=180, y=288, width=90, height=96)

        button_mul = tkinter.Button(self.bootom_frame, text='×', bd='0', font=('微软雅黑', 20), bg='#69B3AD',
                                    fg='#FFFEFF', command=lambda: self.pressOperation('*'))
        button_mul.place(x=270, y=288, width=90, height=96)

        button_point = tkinter.Button(self.bootom_frame, text='.', bd='0', font=('微软雅黑', 20), bg='#429488',
                                      fg='#FFFEFF', command=lambda: self.pressNum('.'))
        button_point.place(x=0, y=384, width=90, height=96)

        button_0 = tkinter.Button(self.bootom_frame, text='0', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('0'))
        button_0.place(x=90, y=384, width=90, height=96)

        button_eq = tkinter.Button(self.bootom_frame, text='=', bd='0', font=('微软雅黑', 40), bg='#69B3AD',
                                   fg='#FFFEFF', command=lambda: self.pressEqual())
        button_eq.place(x=180, y=384, width=180, height=96)

        button_div = tkinter.Button(self.bootom_frame, text='÷', bd='0', font=('微软雅黑', 20), bg='#69B3AD',
                                    fg='#FFFEFF', command=lambda: self.pressOperation('/'))
        button_div.place(x=270, y=384, width=90, height=96)


    def pressC(self):
        if self.flag == False:
            pass
        else:
            self.calList.clear()
            self.result_panel1.set('')
            self.result_panel2.set(0)
            self.flag == False


    def pressBack(self):
        result = self.result_panel2.get()
        result = result[:-1]
        self.calList.clear()
        self.calList.append(result)
        if self.calList[0] == '':
            self.result_panel2.set(0)
        else:
            self.result_panel2.set(''.join(self.calList))

    def pressLeft(self):
        self.calList.append('(')
        self.result_panel2.set(''.join(self.calList))

    def pressRight(self):
        self.calList.append(')')
        self.result_panel2.set(''.join(self.calList))

    def pressNum(self, num):
        oldNum = self.result_panel2.get()
        if oldNum == '0' and self.flag == False:
            if num == '.':
                num = '0.'
            self.result_panel2.set(num)
        else:
            if self.flag == True and oldNum[0] != '(':
                if len(self.calList) == 1:
                    self.result_panel2.set(num)
                    self.calList.clear()
                    self.calList.append(num)
                else:
                    self.calList.append(num)
                    self.result_panel2.set(''.join(self.calList).
                                           replace('*', '×').
                                           replace('/', '÷'))
                self.flag = False
            else:
                    self.flag = False
                    newNum = oldNum + num
                    self.result_panel2.set(newNum)
                    self.calList.clear()
                    self.calList.append(newNum)


    def pressOperation(self, operation):
        num = self.result_panel2.get()
        if num[-1] in '+-÷×^%':
            self.format = False
        if len(num) > 0:
            if num[0] == '(' and len(num) != 1:
                self.calList.clear()
                self.calList.append('(' + num[1:])
            else:
                self.calList.clear()
                self.calList.append(num)

        self.isPressOperation = True
        self.calList.append(operation)
        self.result_panel2.set(''.join(self.calList).replace('/','÷').replace('*','×'))

    def pressEqual(self):
        if self.format == False:
            self.format = True
            try:
                raise FError("Format error")
            except FError:
                self.result_panel2.set('Operator error')
                self.calList.clear()
                self.result_panel1.set('')
                return
        try:
            if len(self.calList) != 0:
                self.result = round(eval(''.join(self.calList).replace('÷', '/').
                                         replace('×', '*')), 3)
                self.result_panel2.set(self.result)
                self.result_panel1.set(''.join(self.calList))
                self.calList.clear()
                self.calList.append(str(self.result))
                self.flag = True
            else:
                self.result_panel1.set(0)

        except SyntaxError:
            self.result_panel2.set('No number')
            self.calList.clear()
            self.result_panel1.set('')
        except ZeroDivisionError:
            self.result_panel2.set('The divisor cannot be 0')
            self.calList.clear()
            self.result_panel1.set('')
        except:
            self.result_panel2.set('ERROR')
            self.calList.clear()
            self.result_panel1.set('')


    def Mouse_Press3(self, e):
        global color_list
        color_list = ['#6495ed', '#8b008b', '#00ced1']
        if self.color_index == len(color_list):
            self.color_index = 0
        e.widget['bg'] = color_list[self.color_index]
        self.color_index += 1


if __name__ == '__main__':
    calculator = MyCalculator(360, 680, 'Mycalculator')
    calculator.set_label()
    calculator.set_span()
    root.mainloop()
