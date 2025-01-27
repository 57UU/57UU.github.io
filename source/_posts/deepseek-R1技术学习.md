---
title: deepseek-R1技术学习
date: 2025-01-22 21:10:18
tags: 
    - LLM
    - AI
---
# 引言
最近`deepseek-r1`模型发布了，相关的技术细节也一同被发布。于是花了几天时间读了一下这篇论文*DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*


# 正文
DeepSeek-R1-zero仅仅只使用了无监督的强化学习，就达到了相当高的水平。在深度学习高度依赖各种数据标记的大环境下，deepseek-r1-zero展现出了一种新的思路。

这里引用原文：
> our goal is to explore the potential of LLMs to develop reasoning capbility without any supervised data.

## Reward建模

reward设计有以下两处：
- 正确奖励
- 格式奖励

### 正确奖励
这里很有意思，只奖励结果。结果正确就满分，错误就得不到一点奖励。

> we find that the neural reward model may suffer from reward hacking in the large-scale reinforcement learning process.

如果奖励过程，很容易让神经网络学到骗分技巧，而不是真正的实力。

对于编程题，也可以通过编译、运行，判断结果准确性。
### 格式奖励
因为模型需要将思考过程与最终结果分别输出，因此需要奖励模型的输出格式。

## Train Input

`训练模板`只要求模型产生一个思维链。不会显示的提醒模型进行反思、提示。

##

//TODO

# 相关知识

## KL散度
KL散度是一种衡量两个概率分布之间差异的方法。

$$
\begin{aligned}
    &\text{For distrubtion } p \text{ and } q:\\
    &D_{KL}(p||q) = \sum_{x \in \mathcal{X}} p(x) \log \frac{p(x)}{q(x)}
\end{aligned}
$$
这乍一看和交叉熵损失函数很像，但是他们有一个显著区别，我们将这个式子变形:
$$
\begin{aligned}
    D_{KL}(p||q) &=  \sum_{x \in \mathcal{X}} p(x) \log p(x) - \sum_{x \in \mathcal{X}} p(x) \log q(x)\\
    &=H(p,q) - H(p)\\
\end{aligned}
$$
其中$H(p,q)$是$p$和$q$的交叉熵，$H(p)$是$p$的熵。

因此，我们可以将KL散度理解为$p$和$q$之间的相对熵，而交叉熵损失函数则是$p$和$q$之间的绝对熵。

## 基于策略的强化学习
不同于基于值函数的确定性强化学习(eg. Q-Learning)，基于策略的强化学习是一种基于概率的强化学习方法，它通过学习一个策略函数来控制智能体的行为。

- 值函数：$\pi:s\rightarrow a$
- 策略函数：$\pi_\theta(a|s)=p(a|s;\theta),\text{the probability of taking the action in the state}$

我们的目标函数如下$J(\theta)$:
$$
\max_\theta J(\theta) = \max_\theta \sum_\tau P(\tau;\theta)R(\tau)
$$
其中$\tau$是一个轨迹（一系列action），$\theta$是策略函数的参数，$P(\tau;\theta)$是轨迹的概率，$R(\tau)$是轨迹的奖励。

意思就是希望最大化奖励的期望。

而$P(\tau;\theta)$又可以定义如下：
$$
P(\tau;\theta) = \prod_{t=0}^T P(s_{t+1}|s_{t},a_t) \pi_\theta(a_t|s_t)
$$

表示为状态转移概率和动作选择概率的乘积，因为状态和动作决定轨迹

我们可以使用样本进行估计，利用如下梯度更新规则：
$$
\theta_{k+1} = \theta_k + \alpha \nabla_\theta J(\theta_k)
$$

对于离散型动作空间，可以使用softmax策略：
$$
\pi_\theta(a|s) = \frac{\exp\{\phi(s,a)^T \theta\}}{\sum_{a' \in A}\exp\{\phi(s,a')^T \theta\}}
$$
其中$\phi(s,a)$是对状态-动作pair$<s,a>$进行特征提取后得到的向量，因此$\phi(s,a)^T \theta$代表两个向量的内积，越相似，内积越大，表明这个动作的偏好程度越大。

值得注意的是，$\phi$函数通常也是一个神经网络，通过强化学习，联合优化，也会不断改进$\phi$函数与$\theta$的配合程度，使其越来越准确。

## PPO&GRPO

简单来说，这就是一种改进的策略梯度算法。平衡了速度、严谨性和可用性，成为了强化学习领域的主流算法之一。

该算法有点复杂，建议阅读[参考资料](#参考资料)


# 后记
这篇论文其实还是很通俗易懂的，不仅英语表达很基础，论文中也没有晦涩难懂的概念，但又展现了出色的创造力与深度，很值得一看。

# 参考资料

- [DeepSeek-R1](https://github.com/deepseek-ai/DeepSeek-R1/blob/main/DeepSeek_R1.pdf)
- [Proximal Policy Optimization (PPO) 算法理解：从策略梯度开始](https://zhuanlan.zhihu.com/p/614115887)
- [[Deepseek v3技术报告学习] 4.GRPO](https://zhuanlan.zhihu.com/p/15922703850)

