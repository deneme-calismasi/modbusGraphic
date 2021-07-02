# File: canvasitems.py
#    http://infohost.nmt.edu/tcc/help/pubs/tkinter//canvas.html
#    http://www.tcl.tk/man/tcl8.5/TkCmd/ttk_scale.htm#M-value
# Ref:
#    'Python and Tkinter Programming' by John Grayson, p44
#        http://manning.com/grayson/
#    Active state recipe with example of labelled ttk.Scale
#        http://code.activestate.com/recipes/577636-color-study-1/
#
# The following behaviours didn't work in Windows 7 using the
# original Tcl demo and are not implemented here:
#
#    Button-2 drag:  reposition view
#    Button-3 drag:  overstroke of a selected area
#    Ctrl-f:         print of overstroke area

from tkinter import *
from tkinter import ttk
from demopanels import MsgPanel, SeeDismissPanel


class CanvasItemsDemo(ttk.Frame):
    # define colours
    BLUE = 'DeepSkyBlue'
    RED = 'red'
    BISQUE = 'bisque3'
    GREEN = 'SeaGreen3'
    HIGHLIGHT = 'SteelBlue2'

    # define fonts
    FONT1 = ('Helv', 12)
    FONT2 = ('Helv', 24, 'bold')

    def __init__(self, isapp=True, name='canvasitemsdemo'):
        ttk.Frame.__init__(self, name=name)
        self.pack(expand=Y, fill=BOTH)
        self.master.title('Canvas Items Demo')
        self.isapp = isapp

        self._create_widgets()

    def _create_widgets(self):
        if self.isapp:
            MsgPanel(self,
                     ["This window contains a canvas widget with examples of the ",
                      "various kinds of items supported by canvases.  The following ",
                      "operations are supported:\n",
                      "\tItem Highlight:\titem under mouse pointer is highlighted.\n"
                      "\tButton-1 drag:\tmoves item under pointer."])

            SeeDismissPanel(self)

        self._create_demo_panel()

    def _create_demo_panel(self):
        demoPanel = Frame(self)
        demoPanel.pack(side=TOP, fill=BOTH, expand=Y)

        self.canvas = self._create_canvas(demoPanel)

        # draw items
        self._draw_lines()
        self._draw_curves()
        self._draw_polygons()
        self._draw_rectangles()
        self._draw_ovals()
        self._draw_text()
        self._draw_arcs()
        self._draw_bitmaps()
        self._draw_windows()

        self._add_bindings()

    def _create_canvas(self, parent):
        c = Canvas(scrollregion='0c 0c 30c 24c', width='15c',
                   height='10c', relief=SUNKEN, borderwidth=2)

        # Draw a 3x3 rectangular grid.
        c.create_rectangle('0c 0c 30c 24c', width=2)
        c.create_line('0c 8c 30c 8c', width=2)
        c.create_line('0c 16c 30c 16c', width=2)
        c.create_line('10c 0c 10c 24c', width=2)
        c.create_line('20c 0c 20c 24c', width=2)

        # add scrollbars
        hscroll = Scrollbar(orient=HORIZONTAL, command=c.xview)
        vscroll = Scrollbar(orient=VERTICAL, command=c.yview)
        c['xscrollcommand'] = hscroll.set
        c['yscrollcommand'] = vscroll.set

        # position and define resize behaviour
        c.grid(in_=parent, sticky='news',
               row=0, rowspan=1, column=0, columnspan=1)
        vscroll.grid(in_=parent, row=0, column=1,
                     rowspan=1, columnspan=1, sticky='news')
        hscroll.grid(in_=parent, row=1, column=0,
                     rowspan=1, columnspan=1, sticky='news')
        parent.grid_rowconfigure(0, weight=1, minsize=0)
        parent.grid_columnconfigure(0, weight=1, minsize=0)

        return c

    # ===================================================================================
    # Canvas item drawing routines
    # ===================================================================================
    def _draw_lines(self):
        c = self.canvas

        c.create_text('5c .2c', text='Lines', anchor=N)
        c.create_line('1c 1c 3c 1c 1c 4c 3c 4c', width='2m',
                      fill=self.BLUE, cap='butt', join='miter',
                      tags=('item',))  # Z
        c.create_line('4.67c 1c 4.67c 4c', arrow=LAST,
                      tags=('item',))  # line w/one arrow
        c.create_line('6.33c 1c 6.33c 4c', arrow=BOTH,
                      tags=('item'))  # line with two arrows

        # maze
        line = ['5c 6c 9c 6c 9c 1c 8c 1c 8c 4.8c 8.8c 4.8c 8.8c 1.2c ',
                '8.2c 1.2c 8.2c 4.6c 8.6c 4.6c 8.6c 1.4c 8.4c 1.4c 8.4c 4.4c']
        c.create_line(''.join(line), width=3, fill=self.RED, tags=('item',))

        # stippled line
        c.create_line('1c 5c 7c 5c 7c 7c 9c 7c', width='.5c', stipple='gray25',
                      arrow=BOTH, arrowshape=(15, 15, 7), tags=('item',))

        # 'M' shape
        c.create_line('1c 7c 1.75c 5.8c 2.5c 7cc 3.25c 5.8c 4c 7c',
                      width='.5c', cap=ROUND, join=ROUND, tags=('item',))

    def _draw_curves(self):
        c = self.canvas

        c.create_text('15c .2c', text='Curves (smoothed lines', anchor=N)

        # curved
        c.create_line('11c 4c 11.5c 1c 13.5c 1c 14c 4c', smooth='on',
                      fill=self.BLUE, tags=('item',))

        # snake with arrows
        c.create_line('15.5c 1c 19.5c 1.5c 15.5c 4.5c 19.5c 4c',
                      smooth='on', arrow=BOTH, width=3, tags=('item',))

        # stippled infinity
        line = ['12c 6c 13.5c 4.5c 16.5c 7.5c 18c 6c ',
                '16.5c 4.5c 13.5c 7.5c 12c 6c']
        c.create_line(''.join(line), smooth='on', width='3m', stipple='gray25',
                      cap=ROUND, fill=self.RED, tags=('item',))

    def _draw_polygons(self):
        c = self.canvas

        c.create_text('25c .2c', text='Polygons', anchor=N)

        # 4 pointed star
        poly = ['21c 1.0c 22.5c 1.75c 24c 1.0c 23.25c 2.5c ',
                '24c 4.0c 22.5c 3.25c 21c 4.0c 21.75c 2.5c']
        c.create_polygon(''.join(poly), fill=self.GREEN,
                         outline='black', width=4, tags=('item',))

        # roller-coaster
        poly = ['25c 4c 25c 4c 25c 1c 26c 1c 27c 4c 28c 1c ',
                '29c 1c 29c 4c 29c 4c']
        c.create_polygon(''.join(poly), fill=self.RED, smooth='on',
                         tags=('item',))

        # stippled blocks
        poly = ['22c 4.5c 25c 4.5c 25c 6.75c 28c 6.75c ',
                '28c 5.25c 24c 5.25c 24c 6.0c 26c 6c 26c 7.5c 22c 7.5c ']
        c.create_polygon(''.join(poly), stipple='gray25',
                         outline='black', tags=('item',))

    def _draw_rectangles(self):
        c = self.canvas

        c.create_text('5c 8.2c', text='Rectangles', anchor=N)

        # empty square
        c.create_rectangle('1c 9.5c 4c 12.5c', outline=self.RED,
                           width='3m', tags=('item',))

        # filled, outlined block
        c.create_rectangle('0.5c 13.5c 4.5c 15.5c', fill=self.GREEN,
                           tags=('item',))

        # stipple filled, non-outlined block
        c.create_rectangle('6c 10c 9c 15c', outline='',
                           stipple='gray25', fill=self.BLUE,
                           tags=('item',))

    def _draw_ovals(self):
        c = self.canvas

        c.create_text('15c 8.2c', text='Ovals', anchor=N)

        # empty circle
        c.create_oval('11c 9.5c 14c 12.5c', outline=self.RED,
                      width='3m', tags=('item',))

        # filled, outlined oval
        c.create_oval('10.5c 13.5c 14.5c 15.5c', fill=self.GREEN,
                      tags=('item',))

        # stipple filled, non-outlined oval
        # Note: the stipple does not work under Windows
        #       (Grayson, p289)
        c.create_oval('16c 10c 19c 15c', outline='',
                      fill=self.BLUE, stipple='gray25',
                      tags=('item',))

    def _draw_text(self):
        c = self.canvas

        c.create_text('25c 8.2c', text='Text', anchor=N)
        c.create_rectangle('22.4c 8.9c 22.6c 9.1c')
        txt = ["A short string of text, word-wrapped, justified left, ",
               "and anchored north (at the top).  The rectangles show ",
               "the anchor points for each piece of text."]
        c.create_text('22.5c 9c', anchor=N, font=self.FONT1, width='4c',
                      text=''.join(txt), tags=('item',))

        c.create_rectangle('25.4c 10.9c 25.6c 11.1c')
        txt = ["Several lines,\n each centered\n",
               "individually,\nand all anchored\nat the left edge."]
        c.create_text('25.5c 11c', anchor=W, font=self.FONT1,
                      fill=self.BLUE, text=''.join(txt), tags=('item',))

        # Note: the stipple does not work well under Windows,
        #       you get a stippled box with no colour rather
        #       than purely stippled text; also, it will not
        #       drag cleanly. The Tk manual states:
        #        "Note that stipples are not well supported on platforms
        #         that do not use X11 as their drawing API."
        c.create_rectangle('24.9c 13.9c 25.1c 14.1c')
        c.create_text('25c 14c', font=self.FONT2, anchor=CENTER,
                      fill=self.RED, stipple='gray50',
                      text='Stippled characters', tags=('item',))

    def _draw_arcs(self):
        c = self.canvas

        c.create_text('5c 16.2c', text='Arcs', anchor=N)

        # ellipse with missing wedge
        c.create_arc('0.5c 17c 7c 20c', fill=self.GREEN,
                     outline='black', start=45, extent=270,
                     style='pieslice', tags=('item',))

        # open-ended circle with stippled outline
        # Note: stipple does not work under Windows
        c.create_arc('6.5c 17c 9.5c 20c', width='4m', style='arc',
                     outline=self.BLUE, start=135, extent=270,
                     outlinestipple='gray25',
                     tags=('item',))

        # rounded pie-slice
        c.create_arc('0.5c 20c 9.5c 24c', width='4m', style='pieslice',
                     fill='', outline=self.RED, start=225, extent=-90,
                     tags=('item',))

        # partial ellipse
        c.create_arc('5.5c 20.5c 9.5c 23.5c', width='4m', style='chord',
                     fill=self.BLUE, outline='', start=45, extent=270,
                     tags=('item',))

    def _draw_bitmaps(self):
        c = self.canvas

        c.create_text('15c 16.2c', text='Bitmaps', anchor=N)

        c.create_bitmap('13c 20c', tags=('item',),
                        bitmap='@images/face.xbm')

        c.create_bitmap('17c 18.5c', tags=('item',),
                        bitmap='@images/noletter.xbm')

        c.create_bitmap('17c 21.5c', tags=('item',),
                        bitmap='@images/letters.xbm')

    def _draw_windows(self):
        c = self.canvas

        c.create_text('25c 16.2c', text='Windows', anchor=N)
        c.create_text('21c 17.9c', text='Button:', anchor='sw')
        btn = ttk.Button(c, text='Press Me', command=self._button_press)
        c.create_window('21c 18c', window=btn, anchor='nw', tags=('item',))

        c.create_text('21c 20.9c', text='Entry:', anchor='sw')
        entry = ttk.Entry(c, width=20)
        entry.insert(END, 'Edit this string')
        c.create_window('21c 21c', window=entry, anchor='nw', tags=('item',))

        c.create_text('28.5c, 17.4c', text='Scale:', anchor=S)
        scale = ttk.Scale(c, from_=0, to=100, length='6c', orient=VERTICAL,
                          command=self._update_scale_value)
        c.create_text('27.5c, 17.4c', text='000', anchor=N, tags=('scalevalue',))
        c.create_window('28.5c 17.5c', window=scale, anchor=N, tags=('item',))

    # ===================================================================================
    # Commands - the 'evt' object passed in is the originating widgets value or None,
    #            not the full Event object generated by a bind
    # ===================================================================================
    def _button_press(self):
        # display some text, wait a few seconds, then remove it
        item = self.canvas.create_text('25c 18.1c', text='Ouch!!',
                                       fill='red', anchor=N)
        self.canvas.after(500, self.canvas.delete, item)

    def _update_scale_value(self, evt):
        # update value as slider is moved
        value = int(float(evt))
        self.canvas.itemconfigure('scalevalue', text='{:>3}'.format(value))

    # ===================================================================================
    # Bindings
    # ===================================================================================
    def _add_bindings(self):
        c = self.canvas

        # behaviour confined to canvas objects with 'item' tag
        c.tag_bind('item', '<Any-Enter>', self._item_enter)
        c.tag_bind('item', '<Any-Leave>', self._item_leave)

        c.tag_bind('item', '<1>', self._item_start_drag)
        c.tag_bind('item', '<B1-Motion>', self._item_drag)

    # ===================================================================================
    # Bound methods
    # ===================================================================================
    def _item_enter(self, evt):
        # highlight the item under the mouse pointer
        c = self.canvas
        c.__restoreItem = None  # ID of item to be restored
        c.__restoreOpts = None  # item options to be restored

        itemType = c.type(CURRENT)  # current object's type
        if itemType == 'window': return  # ignore windows

        c.__restoreItem = c.find_withtag('current')
        opt = ''  # option to be used for highlight

        if itemType == 'bitmap':
            bg = c.itemconfigure(CURRENT, 'background')[4]
            opt = 'background'
            c.__restoreOpts = {opt: bg}
        else:
            fill = c.itemconfigure(CURRENT, 'fill')[4]

            # if the item has no fill, highlight it's outline
            if not fill and itemType in ('rectangle', 'arc', 'oval'):
                outline = c.itemconfigure(CURRENT, 'outline')[4]
                opt = 'outline'
                c.__restoreOpts = {opt: outline}
            else:  # use it's fill option for the highlight
                opt = 'fill'
                c.__restoreOpts = {opt: fill}

        # apply highlight colour to current item
        c.itemconfigure(CURRENT, {opt: self.HIGHLIGHT})

    def _item_leave(self, evt):
        # remove highlight from item
        c = self.canvas

        if c.__restoreItem == c.find_withtag(CURRENT):
            c.itemconfigure(c.__restoreItem, c.__restoreOpts)

    # Note: under Windows, the stippled text item will not
    #       drag cleanly. The Tk manual states:
    #         "Note that stipples are not well supported on platforms
    #          that do not use X11 as their drawing API."
    def _item_start_drag(self, evt):
        # save drag start coordinates
        c = self.canvas

        c.__lastX = c.canvasx(evt.x)
        c.__lastY = c.canvasy(evt.y)

    def _item_drag(self, evt):
        # the item moves (is dragged) with the mouse
        c = self.canvas

        x = c.canvasx(evt.x)
        y = c.canvasy(evt.y)
        c.move(CURRENT, x - c.__lastX, y - c.__lastY)
        c.__lastX = x
        c.__lastY = y


if __name__ == '__main__':
    CanvasItemsDemo().mainloop()
