from viztracer import VizTracer
import heartrate
import snoop

tracer = VizTracer()
tracer.start()
heartrate.trace(browser='True')

# Something happens here
@snoop
def factorial(x):
    if(x==1):
        return 1
    else:
        return (x*factorial(x-1))

if __name__=="__main__":
    num=5
    print(factorial(5))
tracer.stop()
tracer.save()