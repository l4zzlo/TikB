from flask_appbuilder.widgets import ListWidget


class MyListWidget(ListWidget):
     template = 'widgets/custom.html'