
# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# ax = plt.gca()
# [ax.spines[i].set_visible(False) for i in ["top", "right"]]


def gatt(data):
	"""
	甘特图
	:param data: m行n列，第1行工序编号，值加工时间
	:return:
	"""
	makespan = makespan_value(data)
	left = makespan_left(data)
	font_size = 8
	if data.shape[1] <= 30:
		font_size = 10
	if data.shape[0] <= 4:
		font_size = 10
	for i in range(1, data.shape[0]):
		for j in range(data.shape[1]):
			if data[i, j] != 0:
				plt.barh(i, data[i, j], left=left[i, j])
				plt.text(left[i, j] + data[i, j] / 8, i, r"$J_{%s}$" % int(data[0, j]), color="k", size=font_size)
	plt.plot([makespan] * (left.shape[0] + 1), range(left.shape[0] + 1), 'r--', alpha=0.4)
	plt.text(makespan - 0.5, 0, r"$Makespan={%s}$" % np.round(makespan, 2), ha="right", fontdict={"size": 12})
	plt.yticks(range(1, left.shape[0]), range(1, left.shape[0]))
	plt.ylabel(r"$Machine$ $Number$", fontsize=12)
	plt.xlabel(r"$Time$", fontsize=12)


def makespan(data):
	"""
	工件某工序的完成时间
	:param data: m行n列，第1行工序编号，值加工时间
	:return:makespan
	"""
	makespan = np.zeros_like(data)
	for i in range(makespan.shape[0]):
		for j in range(makespan.shape[1]):
			if i == 0:
				makespan[i, j] = data[i, j]
			if i == 1:
				makespan[i, j] = np.sum(data[1, :j + 1])
			if j == 0 and i != 0:
				makespan[i, j] = np.sum(data[1:i + 1, j])
	for i in range(2, makespan.shape[0]):
		for j in range(1, makespan.shape[1]):
			makespan[i, j] = data[i, j] + max(makespan[i, j - 1], makespan[i - 1, j])
	return makespan


def makespan_value(data):
	"""
	最大生产流程时间
	:param data: m行n列，第1行工序编号，值加工时间
	:return:makespan_value
	"""
	makespan_value = makespan(data)[-1, -1]
	return makespan_value


def makespan_left(data):
	"""
	工件某工序的开始时间
	:param data: m行n列，第1行工序编号，值加工时间
	:return:left
	"""
	left = makespan(data) - data
	left[0] = data[0]
	return left


def crtd_fs(n, m, low, high):
	"""
	生成流水车间作业数据
	:param n: 工序数目
	:param m: 机器数目
	:param low: 加工时间最小值
	:param high: 加工时间最大值
	:return:data_fs
	"""
	data_fs = np.zeros([m + 1, n], dtype=int)
	data_fs[0] = np.random.permutation(np.arange(1, n + 1))
	data_fs[1:] = np.random.randint(low, high + 1, [m, n])
	data_fs = data_fs[:, np.argsort(data_fs[0])]
	return data_fs


def crtd_hfs(n, s, low, high):
	"""
	生成混合流水车间作业数据
	:param n: 工件数目
	:param s: 2行，第1行工序，第2行对应的并行机数目
	:param low: 加工时间最小值
	:param high: 加工时间最大值
	:return:data_hfs
	"""
	data_hfs = np.zeros([n, np.sum(s[1]) + 1], dtype=int)
	data_hfs[:, 0] = np.random.permutation(np.arange(1, n + 1))
	data_hfs[:, 1:] = np.random.randint(low, high + 1, [n, np.sum(s[1])])
	data_hfs = data_hfs[np.argsort(data_hfs[:, 0]), :]
	return data_hfs


def crtd_moore(n, low, high):
	"""
	生成单机作业数据
	:param n: 工序数目
	:param low: 加工时间最小值
	:param high: 加工时间最大值
	:return:data_moore
	"""
	data_moore = np.zeros([3, n], dtype=int)
	data_moore[0] = np.random.permutation(np.arange(1, n + 1))
	data_moore[2] = np.random.randint(low, high + 1, n)
	data_moore[1] = data_moore[2] + np.random.randint(n * low, n*low + high + 1, n)
	data_moore = data_moore[:, np.argsort(data_moore[0])]
	return data_moore

