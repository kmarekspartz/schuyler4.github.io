import matplotlib.pyplot as plt
import numpy as np

# Linear Plot and Derivative
x = np.linspace(0, 10, num=10)
linear_y = np.linspace(0, 10, num=10)

derivative = np.ones(10)

plt.plot(x, linear_y, label='Function', color='red')
plt.plot(x, derivative, label='Derivative', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Function and Its Derivative')
plt.legend()
plt.savefig('./pictures/linear-derivative.png')
plt.clf()

# Exponential Plot and Derivative
exp_x = np.linspace(0, 1, num=20)
exp_y = np.exp(exp_x)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Exponential Function and Its Derivative')
plt.plot(exp_x, exp_y, label='Function', color='red')
plt.scatter(exp_x, exp_y, label='Derivative')
plt.legend()
plt.savefig('./pictures/exponential-derivative.png')
plt.clf()

# Sinusoid Plot and Derivative
sin_x = np.linspace(0, 4*np.pi, num=100)
sin_y = np.sin(sin_x)
derivative_y = np.cos(sin_x)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sinusoid Function and Its Derivative')
plt.plot(sin_x, sin_y, label='Function', color='red')
plt.plot(sin_x, derivative_y, label='Derivative', color='blue')
plt.legend()
plt.savefig('./pictures/sinusoid-derivative.png')
plt.clf()

# Constant Plot and Integral
x = np.linspace(0, 10, num=10)
integral = np.linspace(0, 10, num=10)

constant = np.ones(10)

plt.plot(x, integral, label='Integral', color='red')
plt.plot(x, constant, label='Function', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Constant Function and Its Integaral')
plt.legend()
plt.savefig('./pictures/constant-integral.png')
plt.clf()

# RC Discharge
tt = np.linspace(0, 6, num=1000)
v = np.exp(-tt)

plt.plot(tt, v)
plt.xlabel('time (s)')
plt.ylabel('Voltage (V)')
plt.title('RC Circuit Voltage')
plt.savefig('./pictures/rc-voltage.png')
plt.clf()

plt.plot(tt, v)
plt.xlabel('time (s)')
plt.ylabel('Current (A)')
plt.title('RC Circuit Current')
plt.savefig('./pictures/rc-current.png')
plt.clf()

# Resistor IV Curve
RESISTOR_VALUE = 1000
vv = np.linspace(0, 1, num=1000)
ii = vv/RESISTOR_VALUE

plt.plot(vv, ii)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.title('1000 ohm Resistor Curve Trace')
plt.savefig('./pictures/resistor-IV.png')
