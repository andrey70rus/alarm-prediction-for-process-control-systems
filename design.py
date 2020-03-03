
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from numpy import genfromtxt

pg.mkQApp()

pw = pg.PlotWidget()
pw.setBackground((128,128,128,25))
pw.show()
pw.setWindowTitle('pyqtgraph example: MultiplePlotAxes')
p1 = pw.plotItem
p1.setLabels(left='axis 1')

## create a new ViewBox, link the right axis to its coordinate system
p2 = pg.ViewBox()
p1.showAxis('right')
p1.scene().addItem(p2)
p1.getAxis('right').linkToView(p2)
p2.setXLink(p1)
p1.getAxis('right').setLabel('axis2', color='#0000ff')

## create third ViewBox.
## this time we need to create a new axis as well.
p3 = pg.ViewBox()
ax3 = pg.AxisItem('right')
p1.layout.addItem(ax3, 2, 3)
p1.scene().addItem(p3)
ax3.linkToView(p3)
p3.setXLink(p1)
ax3.setZValue(-10000)
ax3.setLabel('axis 3', color='#ff0000')


## Handle view resizing
def updateViews():
    ## view has resized; update auxiliary views to match
    global p1, p2, p3
    p2.setGeometry(p1.vb.sceneBoundingRect())
    p3.setGeometry(p1.vb.sceneBoundingRect())




updateViews()
p1.vb.sigResized.connect(updateViews)

out_data_real = np.array(genfromtxt('Tin_real.csv'))
in_data_real = np.array(genfromtxt('F_ACS.csv'))
out_test = np.array(genfromtxt('out_test.csv'))

p1.plot(out_data_real, pen = pg.mkPen(color='g', width=3, style=QtCore.Qt.DashLine))
#p2.addItem(pg.PlotCurveItem(in_data_real, pen = pg.mkPen(color='r', width=3)))
#p3.addItem(pg.PlotCurveItem(out_test, pen='r'))

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()