from __init__ import power
import tkinter as tk
import tkinter.messagebox as msgbox


class Power(tk.Tk):
    def window(self) -> None:
        self.title("Python快速幂计算器")
        t = tk.Label(self, text="Python快速幂计算器")
        t.pack(side='top', fill=tk.X)
        w = tk.Label(self, text="左底数,右指数（左^右）")
        w.pack(fill=tk.X)
        l = tk.Label(self, text="递归算法实现")
        l.pack(side='bottom', fill=tk.X)
        self.x = tk.Entry(self)
        self.y = tk.Entry(self)
        self.x.pack(side='left')
        self.y.pack(side='right')
        btn = tk.Button(self, text="计算", command=self.answer)
        btn.pack(fill=tk.X)
        self.mainloop()

    def show_error(self, n) -> None:
        msgbox.showerror(title="ERROR", message=n + "暂不支持负数幂运算与小数幂运算")
    
    def answer(self) -> None:
        self.s1 = int(float(self.x.get()))
        self.s2 = int(float(self.y.get()))
        if self.s1 < 0:
            self.show_error("(底数)")
        if self.s2 < 0:
            self.show_error("(指数)")
        else:
            ans = power(self.s1, self.s2)
            msgbox.showinfo(title="ANSWER", message="结果为：" + str(ans))

if __name__ == "__main__":
    p = Power()
    p.window()