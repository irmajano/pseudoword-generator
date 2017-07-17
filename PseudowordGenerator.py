#!/usr/bin/python
# -*- coding: utf-8-*-
#
# Portuguese Pseudoword Generator
#
# March 2016
# Authors:  Ignacio Rubio <rubiomajano.i@gmail.com>
#           Andreia Schurt Rauber <asrauber@gmail.com>
#           Roshanak Hamidi <roshanak.hamidi@gmail.com>

from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
import random


class Application(Frame):
    """The GUI of the program."""

    def __init__(self, master=None):
        """Constructor for the GUI."""
        Frame.__init__(self, master)
        self.grid()
        self.master.title("Portuguese Pseudoword Generator")

        for r in range(2):
            self.master.rowconfigure(r, weight=1)
        for c in range(2):
            self.master.columnconfigure(c, weight=1)

        Frame1 = LabelFrame(master, text="Pseudoword configuration")
        Frame1.grid(row=0, column=0, sticky=N + W)
        Frame2 = LabelFrame(master, text="Syllable structure")
        Frame2.grid(row=1, column=0, sticky=N + W)
        Frame3 = Frame(master)
        Frame3.grid(row=2, column=0, sticky=S + W)
        Frame4 = LabelFrame(master, text="Output")
        Frame4.rowconfigure(0, weight=1)
        Frame4.grid(row=0, column=1, rowspan=3, sticky=N + S + W)

        self.NumWords = IntVar()
        self.MinNumSyll = IntVar()
        self.MaxNumSyll = IntVar()

        nwlabel = Label(Frame1, text="Number of pseudowords").grid(row=2, column=1, sticky=W)
        txtnw = Entry(Frame1, textvariable=self.NumWords, width=3, justify='center').grid(row=2, column=2)
        minlabel = Label(Frame1, text="Minimum number of syllables").grid(row=3, column=1, sticky=W)
        txtmins = Entry(Frame1, textvariable=self.MinNumSyll, width=3, justify='center').grid(row=3, column=2)
        maxlabel = Label(Frame1, text="Maximum number of syllables").grid(row=4, column=1, sticky=W)
        txtmaxs = Entry(Frame1, textvariable=self.MaxNumSyll, width=3, justify='center').grid(row=4, column=2)

        self.OnsetPeakCoda = IntVar()
        self.OnsetPeak = IntVar()
        self.Peak = IntVar()
        self.PeakCoda = IntVar()
        self.Random = IntVar()

        C1 = Checkbutton(Frame2, text="onset + peak + coda", variable=self.OnsetPeakCoda, anchor=W, \
                         onvalue=1, offvalue=0, height=1, width=23).grid(row=1, column=1)

        C2 = Checkbutton(Frame2, text="onset + peak", variable=self.OnsetPeak, anchor=W, \
                         onvalue=1, offvalue=0, height=1, width=23).grid(row=2, column=1)

        C3 = Checkbutton(Frame2, text="peak", variable=self.Peak, anchor=W, \
                         onvalue=1, offvalue=0, height=1, width=23).grid(row=3, column=1)

        C4 = Checkbutton(Frame2, text="peak + coda", variable=self.PeakCoda, anchor=W, \
                         onvalue=1, offvalue=0, height=1, width=23).grid(row=4, column=1)

        C5 = Checkbutton(Frame2, text="random", variable=self.Random, anchor=W, \
                         onvalue=1, offvalue=0, height=1, width=23).grid(row=5, column=1)

        generate_button = Button(Frame3, text="Generate", width=26, background='green',
                                 command=self.generateButtonClick)
        generate_button.grid(row=1, column=1)

        delete_button = Button(Frame3, text="Delete word(s)", width=26, command=self.deleteButtonClick)
        delete_button.grid(row=2, column=1)

        clear_button = Button(Frame3, text="Clear all", width=26, command=self.clearButtonClick)
        clear_button.grid(row=3, column=1)

        save_button = Button(Frame3, text="Save to file", width=26, command=self.saveButtonClick)
        save_button.grid(row=4, column=1)

        close_button = Button(Frame3, text="Exit", width=26, background='red', command=master.destroy)
        close_button.grid(row=5, column=1)

        scrollbar = Scrollbar(Frame4)
        scrollbar.grid(row=0, column=1, rowspan=3, sticky=N + S)

        self.results_box = Listbox(Frame4, yscrollcommand=scrollbar.set, selectmode=MULTIPLE)
        self.results_box.grid(row=0, column=0, sticky=N + S + W + E)

        scrollbar.config(command=self.results_box.yview)

    def generateButtonClick(self):
        """Action for 'Generate' button + warning messages."""
        words = []
        if self.MinNumSyll.get() > self.MaxNumSyll.get():
            warning = tkinter.messagebox.showwarning('Warning',
                                                     'The minimum number of syllables cannot be greater than the maximum number of syllables.')
            return
        if self.NumWords.get() == 0 or self.MinNumSyll.get() == 0 or self.MaxNumSyll.get() == 0:
            warning = tkinter.messagebox.showwarning('Warning', 'Some variable is missing.')
            return
        if self.NumWords.get() == 0 and self.MinNumSyll.get() == 0 and self.MaxNumSyll.get() == 0:
            warning = tkinter.messagebox.showwarning('Warning', 'You must specify the number of words and syllables.')
            return
        if self.OnsetPeakCoda.get() == 0 and self.OnsetPeak.get() == 0 and self.Peak.get() == 0 and self.PeakCoda.get() == 0 and self.Random.get() == 0:
            warning = tkinter.messagebox.showwarning('Warning', 'At least one syllable structure must be selected.')
            return
        if self.Random.get() == 1:
            for i in range(0, self.NumWords.get()):
                word = Word(self.MinNumSyll.get(), self.MaxNumSyll.get(), 1, 1, 1, 1).generateWord()
                words.append(word)
        else:
            for i in range(0, self.NumWords.get()):
                word = Word(self.MinNumSyll.get(), self.MaxNumSyll.get(), self.OnsetPeakCoda.get(),
                            self.OnsetPeak.get(), self.Peak.get(), self.PeakCoda.get()).generateWord()
                words.append(word)
        for item in words:
            self.results_box.insert(END, item)

    def deleteButtonClick(self):
        """Action for 'Delete' button."""
        items = self.results_box.curselection()
        pos = 0
        for i in items:
            idx = int(i) - pos
            self.results_box.delete(idx, idx)
            pos = pos + 1

    def clearButtonClick(self):
        """Action for 'Clear all' button."""
        self.results_box.delete(0, END)

    def saveButtonClick(self):
        """Action for 'Save' button."""
        title = 'Words_' + str(self.NumWords.get()) + '-' + str(self.MinNumSyll.get()) + '-' + str(
            self.MaxNumSyll.get())
        filename = tkinter.filedialog.asksaveasfilename(filetypes=[('All files', '*')],
                                                        defaultextension='.txt',
                                                        initialfile=title)
        dest = open(filename, 'w')
        for w in self.results_box.get(0, END):
            dest.write(w + '\n')
        dest.close()


class Word(object):
    """Class to generate words."""

    def __init__(self, minNoSyll, maxNoSyll, onsetpeakcoda, onsetpeak, peak, peakcoda):
        """Constructor for a word.

        Args:
            minNoSyll (int): Minimum number of syllables.
            maxNoSyll (int): Maximum number of syllables.
            onsetpeakcoda (int): 1 if this configuration is desired, 0 otherwise
            onsetpeak (int): 1 if this configuration is desired, 0 otherwise
            peak (int): 1 if this configuration is desired, 0 otherwise
            peakcoda (int): 1 if this configuration is desired, 0 otherwise
        """
        self.min = minNoSyll
        self.max = maxNoSyll
        self.opc = onsetpeakcoda
        self.op = onsetpeak
        self.p = peak
        self.pc = peakcoda

    def generateWord(self):
        """Generates a word according to the user's input.

        Returns:
            str: The generated word.
        """
        n = random.randint(self.min, self.max)
        self.word = ""
        while True:
            for i in range(0, n):
                syllable = ''
                while True:
                    s = Syllable(i, n, self.opc, self.op, self.p, self.pc).generateSyllable()
                    if not self.word == '':
                        if not self.word[-1] == s[0]:  # Avoiding letter repetition - compliance rules here
                            syllable = s
                            break
                    else:
                        syllable = s
                        break

                self.word = self.word + syllable
            if not self.wordExists():  # Checking that the generated word is a pseudoword
                return self.word

    def wordExists(self):
        """Checks that the word does not exist.

        Returns:
            bool: True if word exists, False if word does not exist.
        """
        return self.word in dictionary


class Syllable(object):
    """Generates a syllable."""

    def __init__(self, position, numberOfSyllables, onsetpeakcoda, onsetpeak, peak, peakcoda):
        """Constructor for a syllable.

        Args:
            position (int): Position of syllable within word.
            numberOfSyllables (int): Number of syllables in the word being generated.
            onsetpeakcoda (int): 1 if this configuration is desired, 0 otherwise
            onsetpeak (int): 1 if this configuration is desired, 0 otherwise
            peak (int): 1 if this configuration is desired, 0 otherwise
            peakcoda (int): 1 if this configuration is desired, 0 otherwise
        """
        self.pos = position
        self.length = numberOfSyllables
        self.opc = onsetpeakcoda
        self.op = onsetpeak
        self.p = peak
        self.pc = peakcoda

    def generateSyllable(self):
        """Generates a syllable.

        Returns:
            str: The generated syllable.
        """
        while True:
            n = random.randint(0, 20)
            if n < 6:
                if self.p == 1:
                    syllable = self.generatePeakComp()
                    self.pos == self.pos + 1
                    return syllable
            if 6 <= n <= 10:
                if self.op == 1:
                    syllable = self.generateOnsetPeak()
                    if self.pos == 0:
                        if not syllable.startswith(('nh', 'lh', 'vr', 'tl', 'ss', 'rr', 'ç')):
                            self.pos == self.pos + 1
                            return syllable
                    else:
                        self.pos == self.pos + 1
                        return syllable
            if 11 <= n <= 15:
                if self.pc == 1:
                    syllable = self.generatePeakCoda()
                    self.pos == self.pos + 1
                    return syllable
            if 16 <= n <= 20:
                if self.opc == 1:
                    syllable = self.generateOnsetPeakCoda()
                    if self.pos == 0:
                        if not syllable.startswith(('nh', 'lh', 'vr', 'tl', 'ss', 'rr', 'ç')):
                            self.pos == self.pos + 1
                            return syllable
                    else:
                        self.pos == self.pos + 1
                        return syllable

    def generateOnsetComp(self):
        """Generate an onset component of a syllable.

        Returns:
            str: The generated component.
        """
        n = random.randint(1, 602)
        if n < 37:
            return 'p'
        elif n in range(37, 46):
            return 'b'
        elif n in range(46, 117):
            return 't'
        elif n in range(117, 217):
            return 'd'
        elif n in range(217, 268):
            return 'c'
        elif n in range(268, 272):
            return 'qu'
        elif n in range(272, 286):
            return 'g'
        elif n == 286:
            return 'gu'
        elif n in range(287, 303):
            return 'f'
        elif n in range(303, 325):
            return 'v'
        elif n in range(325, 364):
            return 's'
        elif n in range(364, 378):
            return 'ss'
        elif n in range(378, 387):
            return 'ç'
        elif n in range(387, 402):
            return 'z'
        elif n in range(402, 404):
            return 'x'
        elif n == 404:
            return 'ch'
        elif n in range(405, 410):
            return 'j'
        elif n in range(410, 454):
            return 'm'
        elif n in range(454, 489):
            return 'n'
        elif n in range(489, 492):
            return 'nh'
        elif n in range(492, 533):
            return 'r'
        elif n in range(533, 536):
            return 'rr'
        elif n in range(536, 559):
            return 'l'
        elif n in range(559, 562):
            return 'lh'
        elif n in range(562, 564):
            return 'pl'
        elif n in range(564, 575):
            return 'pr'
        elif n == 575:
            return 'ps'
        elif n == 576:
            return 'bl'
        elif n in range(577, 580):
            return 'br'
        elif n == 580:
            return 'tl'
        elif n in range(581, 591):
            return 'tr'
        elif n == 591:
            return 'dr'
        elif n == 592:
            return 'fl'
        elif n == 593:
            return 'fr'
        elif n == 594:
            return 'vr'
        elif n == 595:
            return 'cl'
        elif n in range(596, 598):
            return 'cr'
        elif n == 598:
            return 'gl'
        elif n in range(599, 603):
            return 'gr'

    def generatePeakComp(self):
        """Generate a peak component of a syllable (or peak syllable configuration).

        Returns:
            str: The generated component.
        """
        n = random.randint(1, 544)
        if n < 4:
            return 'un'
        elif n in range(4, 6):
            return 'um'
        elif n in range(6, 13):
            return 'on'
        elif n in range(13, 16):
            return 'om'
        elif n in range(16, 20):
            return 'in'
        elif n in range(20, 22):
            return 'im'
        elif n in range(22, 25):
            return 'an'
        elif n in range(25, 29):
            return 'am'
        elif n in range(29, 39):
            return 'en'
        elif n in range(39, 44):
            return 'em'
        elif n in range(44, 53):
            return 'ãe'
        elif n in range(53, 159):
            return 'e'
        elif n in range(159, 192):
            return 'o'
        elif n in range(192, 328):
            return 'a'
        elif n in range(328, 405):
            return 'i'
        elif n in range(405, 498):
            return 'u'
        elif n == 498:
            return 'eo'
        elif n in range(499, 501):
            return 'eu'
        elif n in range(501, 504):
            return 'ai'
        elif n in range(504, 510):
            return 'ei'
        elif n in range(510, 514):
            return 'oi'
        elif n == 514:
            return 'ui'
        elif n == 515:
            return 'iu'
        elif n in range(516, 520):
            return 'au'
        elif n in range(520, 522):
            return 'õe'
        elif n in range(522, 525):
            return 'io'
        elif n == 525:
            return 'eo'
        elif n in range(526, 530):
            return 'ia'
        elif n == 530:
            return 'ua'
        elif n in range(531, 545):
            return 'ão'

    def generateCodaMidComp(self):
        """Generate a mid-word coda component of a syllable.

        Returns:
            str: The generated component.
        """
        n = random.randint(1, 163)
        if n < 2:
            return 'p'
        elif n == 2:
            return 'b'
        elif n == 3:
            return 't'
        elif n == 4:
            return 'd'
        elif n == 5:
            return 'c'
        elif n == 6:
            return 'g'
        elif n == 7:
            return 'bs'
        elif n in range(8, 108):
            return 's'
        elif n in range(108, 110):
            return 'z'
        elif n in range(110, 124):
            return 'l'
        elif n in range(124, 164):
            return 'r'

    def generateCodaComp(self):
        """Generate a coda component of a syllable.

        Returns:
            str: The generated component.
        """
        n = random.randint(1, 154)
        if n < 101:
            return 's'
        elif n in range(101, 115):
            return 'l'
        elif n in range(115, 155):
            return 'r'

    def generatePeakCoda(self):
        """Generate a peak+coda syllable configuration.

        Returns:
            str: The generated syllable.
        """
        if not self.pos == self.length - 1:
            syllable = self.generatePeakComp() + self.generateCodaMidComp()
            return syllable
        else:
            syllable = self.generatePeakComp() + self.generateCodaComp()
            return syllable

    def generateOnsetPeak(self):
        """Generate an onset+peak syllable configuration.

        Returns:
            str: The generated syllable.
        """
        syllable = self.generateOnsetComp() + self.generatePeakComp()
        return syllable

    def generateOnsetPeakCoda(self):
        """Generate an onset+peak+coda syllable configuration.

        Returns:
            str: The generated syllable.
        """
        if not self.pos == self.length - 1:
            syllable = self.generateOnsetComp() + self.generatePeakComp() + self.generateCodaMidComp()
            return syllable
        else:
            syllable = self.generateOnsetComp() + self.generatePeakComp() + self.generateCodaComp()
            return syllable


f = open('words.txt', 'r')
global dictionary  # The dictionary of existing words.
dictionary = []
for word in f.readlines():
    dictionary.append(word.lower().strip())

root = Tk()
app = Application(master=root)

app.mainloop()
