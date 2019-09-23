import random;
import numpy as np

def analyzeKeystrokeData(filepath):
	lines = None;
	with open(filepath,"r",encoding="utf-8") as f:
		lines = f.readlines();
	ret = np.random.rand(5)
	return ret