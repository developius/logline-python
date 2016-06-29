from logline import *

logline = LogLine("DF165TEZIC")

if logline.info("test logging from python"):
	print("Info log succeeded")
if logline.success("test logging from python"):
	print("Success log succeeded")
if logline.warning("test logging from python"):
	print("Warning log succeeded")
if logline.fatal("test logging from python"):
	print("Fatal log succeeded")