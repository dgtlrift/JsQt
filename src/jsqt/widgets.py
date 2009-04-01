# encoding: utf8

#
# This file is part of JsQT.
#
# Copyright (C) 2009 Arskom Ltd. www.arskom.com.tr
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#

from jsqt import Base

class Widget(Base):        
    def __init__(self, caller, name, class_name):
        Base.__init__(self, caller, name, class_name)

    def set_geometry_x(self, x):
        self.x = x
    def set_geometry_y(self, y):
        self.y = y
    def set_geometry_w(self, w):
        self.buffer.append('        this.%(self_name)s.setWidth(%(width)s);' % {'self_name': self.name(), 'width': w})
    def set_geometry_h(self, h):
        self.buffer.append('        this.%(self_name)s.setHeight(%(width)s);' % {'self_name': self.name(), 'width': h})

    def get_tag(self):
        return "widget"

class QPushButton(Widget):
    def __init__(self, caller, name, class_name):
        self.type = "qx.ui.form.Button"
        Widget.__init__(self, caller, name, class_name)

        self.register_handlers()
        self.xmltext_handlers[("text", None, "string")] = self.set_text

    def set_text(self, text, *args):
        self.buffer.append('        this.%(self_name)s.setLabel("%(text)s");' % {'self_name': self.name(), 'text': text})


class QLabel(Widget):
    def __init__(self, caller, name, class_name):
        self.type="qx.ui.basic.Label"
        Widget.__init__(self, caller, name, class_name)

        self.register_handlers()
        self.xmltext_handlers[("text", None, "string")] = self.set_text
	
    def js_inst(self):
        Widget.js_inst(self)
        self.buffer.append('        this.%(self_name)s.setAllowGrowX(false);' % {'self_name': self.name()})
        self.buffer.append('        this.%(self_name)s.setAllowGrowY(false);' % {'self_name': self.name()})
        self.buffer.append('        this.%(self_name)s.setAllowShrinkX(false);' % {'self_name': self.name()})
        self.buffer.append('        this.%(self_name)s.setAllowShrinkY(false);' % {'self_name': self.name()})

    def set_text(self, text, *args):
        self.buffer.append('        this.%(self_name)s.setContent("%(text)s");' % {'self_name': self.name(), 'text': text})

class QLineEdit(Widget):
    def __init__(self, caller, name, class_name):
        self.type="qx.ui.form.TextField"
        Widget.__init__(self, caller, name, class_name)

        self.register_handlers()
        self.xmltext_handlers[("echoMode", None, "enum")] = self.set_echoMode
        self.xmltext_handlers[("text", None, "string")] = self.set_text

    def set_text(self, text, *args):
        self.buffer.append('        this.%(self_name)s.setValue("%(text)s");' % {'self_name': self.name(), 'text': text})
    
    def set_echoMode(self, text, *args):
        if text == "QLineEdit::Password":
            self.type = "qx.ui.form.PasswordField"
            self.js_inst()

class QTextEdit(Widget):
    def __init__(self, caller, name, class_name):
        self.type="qx.ui.form.TextArea"
        Widget.__init__(self, caller, name, class_name)

        self.register_handlers()
        self.xmltext_handlers[("text", None, "string")] = self.set_text

    def set_text(self, text, *args):
        self.buffer.append('        this.%(self_name)s.setValue("%(text)s");' % {'self_name': self.name(), 'text': text})
    
class QSpinBox(Widget):
    def __init__(self, caller, name, class_name):
        self.type="qx.ui.form.Spinner"
        Widget.__init__(self, caller, name, class_name)

        self.register_handlers()
        self.xmltext_handlers[("text", None, "string")] = self.set_text
        self.xmltext_handlers[(u'singleStep', None, u'number')] = self.set_single_step
        self.xmltext_handlers[(u'maximum', None, u'number')] = self.set_max
        self.xmltext_handlers[(u'minimum', None, u'number')] = self.set_min
        self.xmltext_handlers[(u'value', None, u'number')] = self.set_text

    def set_text(self, text, *args):
        self.buffer.append('        this.%(self_name)s.setValue(%(text)s);' % {'self_name': self.name(), 'text': text})

    def set_single_step(self, text, *args):
        self.buffer.append('        this.%(self_name)s.setSingleStep(%(text)s);' % {'self_name': self.name(), 'text': text})

    def set_min(self, text, *args):
        self.buffer.append('        this.%(self_name)s.setMin(%(text)s);' % {'self_name': self.name(), 'text': text})

    def set_max(self, text, *args):
        self.buffer.append('        this.%(self_name)s.setMax(%(text)s);' % {'self_name': self.name(), 'text': text})
    
class QDateEdit(Widget):
    def __init__(self, caller, name, class_name):
        self.type="qx.ui.form.DateField"
        Widget.__init__(self, caller, name, class_name)

        self.register_handlers()
        self.xmltext_handlers[("text", None, "string")] = self.set_text

    def set_text(self, text, *args):
        self.buffer.append('        this.%(self_name)s.setValue("%(text)s");' % {'self_name': self.name(), 'text': text})
    

class QCheckBox(Widget):
    def __init__(self, caller, name, class_name):
        self.type="qx.ui.form.CheckBox"
        Widget.__init__(self, caller, name, class_name)

        self.register_handlers()
        self.xmltext_handlers[("text", None, "string")] = self.set_text
        self.xmltext_handlers[("checked", None, "bool")] = self.set_value

    def set_text(self, text, *args):
        self.buffer.append('        this.%(self_name)s.setLabel("%(text)s");' % {'self_name': self.name(), 'text': text})

    def set_value(self, text, *args):
        self.buffer.append('        this.%(self_name)s.setChecked(%(text)s);' % {'self_name': self.name(), 'text': text})

class QRadioButton(Widget):
    def __init__(self, caller, name, class_name):
        self.type="qx.ui.form.RadioButton"
        Widget.__init__(self, caller, name, class_name)

        self.register_handlers()
        self.xmltext_handlers[("text", None, "string")] = self.set_text
        self.xmltext_handlers[("checked", None, "bool")] = self.set_value

    def set_text(self, text, *args):
        self.buffer.append('        this.%(self_name)s.setLabel("%(text)s");' % {'self_name': self.name(), 'text': text})

    def set_value(self, text, *args):
        self.buffer.append('        this.%(self_name)s.setChecked(%(text)s);' % {'self_name': self.name(), 'text': text})

class QComboBox(Widget):
    def __init__(self, caller, name, class_name):
        self.type = "qx.ui.form.SelectBox"
        Widget.__init__(self, caller, name, class_name)

        self.register_handlers()
        self.xmltext_handlers[("text", None, "string")] = self.add_text
    
    def set_text(self, text, *args):
        raise Exception("With ComboBox, add_text must be used.")

    def add_text(self, text, *args):
        self.buffer.append('        this.%(self_name)s.add(new qx.ui.form.ListItem("%(text)s"));' % {'self_name': self.name(), 'text': text})

class Spacer(Widget):
    def __init__(self, caller, name, class_name):
        self.type = "qx.ui.core.Spacer"
        Widget.__init__(self, caller, name, class_name)

        self.register_handlers()

class QAbstractItemView(Widget):
    def __init__(self, caller, name, class_name):
        Widget.__init__(self, caller, name, class_name)

        self.xmltext_handlers[(u'selectionMode', None, u'enum')] = self.set_selection_mode    

    def set_selection_mode(self, mode, *args):
        self.buffer.append("        // FIXME: this.%(self_name)s.getSelectionModel().setSelectionMode(qx.ui.table.selection.Model.%(mode)s);" % {"self_name": self.name(), "mode": mode})

class QListWidget(QAbstractItemView):
    def __init__(self, caller, name, class_name):
        self.type = "qx.ui.form.List"
        QAbstractItemView.__init__(self, caller, name, class_name)

        self.register_handlers()

class QTableWidget(QAbstractItemView):
    def __init__(self, caller, name, class_name):
        self.type="qx.ui.table.Table"
        QAbstractItemView.__init__(self, caller, name, class_name)

        self.register_handlers()