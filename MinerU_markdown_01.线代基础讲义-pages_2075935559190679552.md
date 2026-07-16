## 第一章 行列式

## 1.1行列式的定义

行列式和矩阵是线性代数中的重要概念,其中行列式最早出现于17世纪,其起源于线性方程组的求解,它最早是一种速记的表达式。在很长一段时间内,行列式只是作为解线性方程组的一种工具使用。1850年,英国数学家西尔维斯特在研究方程的个数与未知量的个数不相同的线性方程组时,由于无法使用行列式,所以引入了矩阵的概念。1858年,凯莱在《矩阵论的研究报告》中,系统阐述了关于矩阵的理论。所以从时间上,行列式的概念先于矩阵的概念出现,矩阵的诸多性质也是基于行列式的发展而建立起来的。这也从某种程度上解释了为什么国内线代教材多以行列式作为线代开篇。

引例: 对于一个二元一次方程组

$$
\left\{ \begin{array}{l} a _ {1 1} x _ {1} + a _ {1 2} x _ {2} = b _ {1} \\ a _ {2 1} x _ {1} + a _ {2 2} x _ {2} = b _ {2} \end{array} \right.
$$

根据中学知识容易得到，当 $a_{11}a_{22}-a_{12}a_{21}\neq0$ 时，方程有解

$$
x _ {1} = \frac {b _ {1} a _ {2 2} - a _ {1 2} b _ {2}}{a _ {1 1} a _ {2 2} - a _ {1 2} a _ {2 1}}, \quad x _ {2} = \frac {a _ {1 1} b _ {2} - b _ {1} a _ {2 1}}{a _ {1 1} a _ {2 2} - a _ {1 2} a _ {2 1}}
$$

如果记

$$
D = \left| \begin{array}{c c} a _ {1 1} & a _ {1 2} \\ a _ {2 1} & a _ {2 2} \end{array} \right| = a _ {1 1} a _ {2 2} - a _ {1 2} a _ {2 1}
$$

为便于记忆, 二阶行列式 $D$ 可以按下面的对角线法则来计算

$$
D = \left| \begin{array}{c c} a _ {1 1} & a _ {1 2} \\ a _ {2 1} & a _ {2 2} \end{array} \right| = a _ {1 1} a _ {2 2} - a _ {1 2} a _ {2 1}
$$

引入二阶行列式后，上述方程组的解可以分别表示为

$$
x _ {1} = \frac {D _ {1}}{D}, x _ {2} = \frac {D _ {2}}{D}
$$

其中，

$$
D _ {1} = \left| \begin{array}{l l} b _ {1} & a _ {1 2} \\ b _ {2} & a _ {2 2} \end{array} \right| = b _ {1} a _ {2 2} - b _ {2} a _ {1 2}, \quad D _ {2} = \left| \begin{array}{l l} a _ {1 1} & b _ {1} \\ a _ {2 1} & b _ {2} \end{array} \right| = b _ {2} a _ {1 1} - b _ {1} a _ {2 1}
$$

那么，三阶及更高阶行列式又该如何定义（计算）呢？接下来我们从三元线性方程组入手分析。

$$
\left\{ \begin{array}{l} a _ {1 1} x _ {1} + a _ {1 2} x _ {2} + a _ {1 3} x _ {3} = b _ {1} \\ a _ {2 1} x _ {1} + a _ {2 2} x _ {2} + a _ {2 3} x _ {3} = b _ {2} \\ a _ {3 1} x _ {1} + a _ {3 2} x _ {2} + a _ {3 3} x _ {3} = b _ {3} \end{array} \right.
$$

通过消元法可求得（这里仅分析 $x_{1}$ ）

$$
x _ {1} = \frac {D _ {1}}{D} = \frac {b _ {1} a _ {2 2} a _ {3 3} + a _ {1 2} a _ {2 3} b _ {3} + a _ {1 3} b _ {2} a _ {3 2} - b _ {1} a _ {2 3} a _ {3 2} - a _ {1 2} b _ {2} a _ {3 3} - a _ {1 3} a _ {2 2} b _ {3}}{a _ {1 1} a _ {2 2} a _ {3 3} + a _ {1 2} a _ {2 3} a _ {3 1} + a _ {1 3} a _ {2 1} a _ {3 2} - a _ {1 1} a _ {2 3} a _ {3 2} - a _ {1 2} a _ {2 1} a _ {3 3} - a _ {1 3} a _ {2 2} a _ {3 1}}
$$

三元线性方程组解 $x_{1}$ 的分母和分子可分别写成三阶行列式的形式如下：

$$
D = \left| \begin{array}{l l l} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| = a _ {1 1} a _ {2 2} a _ {3 3} + a _ {1 2} a _ {2 3} a _ {3 1} + a _ {1 3} a _ {2 1} a _ {3 2} - a _ {1 1} a _ {2 3} a _ {3 2} - a _ {1 2} a _ {2 1} a _ {3 3} - a _ {1 3} a _ {2 2} a _ {3 1}
$$

$$
D _ {1} = \left| \begin{array}{c c c} b _ {1} & a _ {1 2} & a _ {1 3} \\ b _ {2} & a _ {2 2} & a _ {2 3} \\ b _ {3} & a _ {3 2} & a _ {3 3} \end{array} \right| = b _ {1} a _ {2 2} a _ {3 3} + a _ {1 2} a _ {2 3} b _ {3} + a _ {1 3} b _ {2} a _ {3 2} - b _ {1} a _ {2 3} a _ {3 2} - a _ {1 2} b _ {2} a _ {3 3} - a _ {1 3} a _ {2 2} b _ {3}
$$

则

$$
x _ {1} = \frac {D _ {1}}{D} = \frac {\left| \begin{array}{l l l} b _ {1} & a _ {1 2} & a _ {1 3} \\ b _ {2} & a _ {2 2} & a _ {2 3} \\ b _ {3} & a _ {3 2} & a _ {3 3} \end{array} \right|}{\left| \begin{array}{l l l} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right|}
$$

很明显，三阶的行列式计算结果相当复杂，更高阶的行列式更是如此。人们开始思考，二阶行列式与三阶行列式之间是否有联系呢？是否能够用二阶行列式来表示（计算）三阶行列式？要是能用低阶行列式去定义（计算）高阶行列式就好了！

为解释这个问题，这里我们先引进两个概念：余子式和代数余子式。

定义: $n$ 阶行列式 $D$ 中, 把元素 $a_{ij}$ 所在的第 $i$ 行和第 $j$ 列的所有元素划去, 余下的 $(n-1)^{2}$ 个元素按原顺序组成的 $n-1$ 阶行列式称为元素 $a_{ij}$ 的余子式, 记作 $M_{ij}$ . 令 $A_{ij} = (-1)^{i+j} M_{ij}$ , 则 $A_{ij}$ 称为元素 $a_{ij}$ 的代数余子式示例 1:

行列式 $D=\begin{vmatrix}0&1&1\\1&0&0\\0&1&2\end{vmatrix}$ 中元素 $a_{21}$ 的余子式为 $M_{21}=\begin{vmatrix}1&1\\1&2\end{vmatrix}=1$ ，而其代数余子式为 $A_{21}=(-1)^{2+1}M_{21}=-1$ .
示例 2:

对于 2 阶行列式 $\begin{vmatrix}a_{11}&a_{12}\\ a_{21}&a_{22}\end{vmatrix}$ ，我们也可以类似定义，第 1 行元素 $a_{11}, a_{12}$ 的代数余子式分别是 $A_{11}=(-1)^{1+1}a_{22},\quad A_{12}=(-1)^{1+2}a_{21}.$ 

这样，2阶行列式 $D_{2}$ 可写成 $D_{2} = \left| \begin{array}{ll}a_{11} & a_{12}\\ a_{21} & a_{22} \end{array} \right| = a_{11}A_{11} + a_{12}A_{12}.$ 

示例 3:

$$
D = \left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| = a _ {1 1} \left| \begin{array}{c c} a _ {2 2} & a _ {2 3} \\ a _ {3 2} & a _ {3 3} \end{array} \right| - a _ {1 2} \left| \begin{array}{c c} a _ {2 1} & a _ {2 3} \\ a _ {3 1} & a _ {3 3} \end{array} \right| + a _ {1 3} \left| \begin{array}{c c} a _ {2 1} & a _ {2 2} \\ a _ {3 1} & a _ {3 2} \end{array} \right|,
$$

其中， $M_{11} = \left| \begin{array}{ll}a_{22} & a_{23}\\ a_{32} & a_{33} \end{array} \right|$ ， $M_{12} = \left| \begin{array}{ll}a_{21} & a_{23}\\ a_{31} & a_{33} \end{array} \right|$ ， $M_{13} = \left| \begin{array}{ll}a_{21} & a_{22}\\ a_{31} & a_{32} \end{array} \right|$ 分别称为元素 $a_{11},a_{12},a_{13}$ 的余子式，并称 $A_{11} = (-1)^{1 + 1}M_{11}, A_{12} = (-1)^{1 + 2}M_{12},A_{13} = (-1)^{1 + 3}M_{13}$ 分别为 $a_{11},a_{12},a_{13}$ 的代数余子式。便可得到，

$$
D = a _ {1 1} A _ {1 1} + a _ {1 2} A _ {1 2} + a _ {1 3} A _ {1 3}
$$

通过这几个示例可以发现两点：第一，行列式总可以按第一行展开来计算；第二，这种用低阶行列式定义高一阶行列式的方法是有一般意义的，按照这种思想，我们给出 $n$ 阶行列式的归纳法定义。

定义：n 阶行列式是由 $n^{2}$ 个元素 $a_{ij}(i,j=1,2,\cdots,n)$ 所决定的一个数.

$$
D _ {n} = \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right|
$$

当 $n = 1$ 时，定义1阶行列式 $D_{1} = \left|a_{11}\right| = a_{11}$ 。假设 $n - 1$ 阶行列式已经定义，则定义 $n$ 阶行列式

$$
D _ {n} = \left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ a _ {2 1} & a _ {2 2} & \dots & a _ {2 n} \\ \vdots & \vdots & & \vdots \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right| = a _ {1 1} A _ {1 1} + a _ {1 2} A _ {1 2} + \dots + a _ {1 n} A _ {1 n}.
$$

上式称为 $n$ 阶行列式 $D_{n}$ 关于第1行的展开式。

这里补充说明两点：第一， $n = 1$ 时，1阶行列式 $\left|a_{11}\right| = a_{11}$ 不能与数的绝对值混淆；第二，行列式的主流定义方式有三种，这里采用容易理解的归纳法，用逆序数来定义行列式的方式不作介绍，考研极少涉及到。

## 1.2 行列式的性质

接下来我们学习行列式的部分性质，以简化行列式的计算。需要向大家强调的是，大家最重要的是要学会如何理解并记忆这些性质，至于严格的证明过程并不要求大家掌握。为了便于大家理解，这里均以3阶行列式为例，事实上对于任意阶行列式以下性质均成立。

性质 1: (行列式行列互换) 行列式中行列互换 (转置), 其值不变.

$$
\left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| = \left| \begin{array}{c c c} a _ {1 1} & a _ {2 1} & a _ {3 1} \\ a _ {1 2} & a _ {2 2} & a _ {3 2} \\ a _ {1 3} & a _ {2 3} & a _ {3 3} \end{array} \right|.
$$

此性质说明, 行列式对于行成立的性质, 对于列也同样成立。以下我们仅对行讨论行列式的性质。
性质 2：行列式中两行（列）对换, 其值变号.

$$
\left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| = - \left| \begin{array}{c c c} a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right|.
$$

推论：行列式中如果有两行（列）元素对应相等，则行列式的值为 0.

性质 3: （线性性质）行列式中某行（列）元素有公因子，可将公因子提到行列式外.

$$
\left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ k a _ {2 1} & k a _ {2 2} & k a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| = k \left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right|.
$$

推论 1：行列式中如果有一行（列）元素全为 0，则行列式的值为 0。

推论 2：行列式中如果有两行（列）元素对应成比例，则行列式的值为 0.

性质 4:（线性性质）行列式中如果有一行（列）的每个元素都由两个数之和组成, 行列式可以拆成两个行列式的和.

$$
\left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} + b _ {2 1} & a _ {2 2} + b _ {2 2} & a _ {2 3} + b _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| = \left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| + \left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ b _ {2 1} & b _ {2 2} & b _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right|.
$$

性质 5:（行列式的倍加）在行列式中, 把某行（列）各元素分别乘非零常数 k, 再加到另一行（列）的对应元素上, 行列式的值不变, 即

$$
\left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ a _ {2 1} & a _ {2 2} & a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right| = \left| \begin{array}{c c c} a _ {1 1} & a _ {1 2} & a _ {1 3} \\ k a _ {1 1} + a _ {2 1} & k a _ {1 2} + a _ {2 2} & k a _ {1 3} + a _ {2 3} \\ a _ {3 1} & a _ {3 2} & a _ {3 3} \end{array} \right|
$$

【例1】设 $\left| \begin{array}{lll}c_1 & b_1 & a_1\\ c_2 & b_2 & a_2\\ c_3 & b_3 & a_3 \end{array} \right| = -2$ ，则 $\left| \begin{array}{lll}a_{1} & 2c_{1} + a_{1} & -a_{1} - b_{1}\\ a_{2} & 2c_{2} + a_{2} & -a_{2} - b_{2}\\ a_{3} & 2c_{3} + a_{3} & -a_{3} - b_{3} \end{array} \right| = \_$ 

【例2】证明： $\left| \begin{array}{ll}a + x & b + y\\ c + z & d + w \end{array} \right| = \left| \begin{array}{ll}a & b\\ c & d \end{array} \right| + \left| \begin{array}{ll}a & y\\ c & w \end{array} \right| + \left| \begin{array}{ll}x & b\\ z & d \end{array} \right| + \left| \begin{array}{ll}x & y\\ z & w \end{array} \right|$ 

【例3】证明： $\left| \begin{array}{lll}ax + by & ay + bz & az + bx\\ ay + bz & az + bx & ax + by\\ az + bx & ax + by & ay + bz \end{array} \right| = (a^3 +b^3)\left| \begin{array}{lll}x & y & z\\ y & z & x\\ z & x & y \end{array} \right|$ 

## 1.3行列式的计算

行列式计算的主要思路是利用行列式的性质和展开定理，化繁为简，化未知为已知，化高阶为低阶。在介绍行列式的定义时，其实已经向大家介绍了行列式按第一行展开的计算公式，这里进一步介绍更具一般性的结论。

## 1.3.1 行列式展开定理

n 阶行列式 D 等于它的任一行（列）的各元素与其对应的代数余子式乘积之和,即

$$
D = a _ {i 1} A _ {i 1} + a _ {i 2} A _ {i 2} + \dots + a _ {i n} A _ {i n} = \sum_ {k = 1} ^ {n} a _ {i k} A _ {i k}
$$

$$
D = a _ {1 j} A _ {1 j} + a _ {2 j} A _ {2 j} + \dots + a _ {n j} A _ {n j} = \sum_ {k = 1} ^ {n} a _ {k j} A _ {k j}
$$

其中， $i,j=1,2,\cdots,n$ 

行列式展开定理的推论：

推论 1：行列式中如果有一行（列）元素全为 0，则行列式的值为 0。

推论 2: $n$ 阶行列式 $D$ 的任一行（列）的各元素与另一行（列）对应元素的代数余子式乘积之和为 0，即

$$
a _ {i 1} A _ {j 1} + a _ {i 2} A _ {j 2} + \dots + a _ {i n} A _ {j n} = \sum_ {k = 1} ^ {n} a _ {i k} A _ {j k} = 0 (i \neq j)
$$

$$
a _ {1 i} A _ {1 j} + a _ {2 i} A _ {2 j} + \dots + a _ {n i} A _ {n j} = \sum_ {k = 1} ^ {n} a _ {k i} A _ {k j} = 0 (i \neq j)
$$

【例1】设行列式 $D = \left| \begin{array}{cccc}3 & -5 & 2 & 1\\ 1 & 1 & 0 & -5\\ -1 & 3 & 1 & 3\\ 2 & -4 & -1 & -3 \end{array} \right|$ ，则求：

(1) $A_{11} + A_{12} + A_{13} + A_{14}$ (2) $A_{11} + A_{12} - 5A_{14}$ (3) $M_{11} + M_{21} + M_{31} + M_{41}$ . 

## 1.3.2 常见行列式计算

从行列式展开公式不难发现，行列式中 0 越多就越容易计算。因此，常用的做法是化零降阶法，利用性质将行列式中某一行（或列）非零的元素尽可能消成零，一般消至剩余一个非零元素，再用行列式展开定理计算。

另外，行列式中有几个很常用的行列式，例如对角行列式、三角行列式、范德蒙德行列式等。它们的结果是已知的，可以拿来当公式用，大家需要牢记。

(1) 主对角行列式:

$$
\left| \begin{array}{c c c c} a _ {1 1} & & & \\ & a _ {2 2} & & \\ & & \ddots & \\ & & & a _ {n n} \end{array} \right| = a _ {1 1} a _ {2 2} \dots a _ {n n}
$$

(2) 主对角线上 (下) 三角行列式:

$$
\left| \begin{array}{c c c c} a _ {1 1} & a _ {1 2} & \dots & a _ {1 n} \\ & a _ {2 2} & \dots & a _ {2 n} \\ & & \ddots & \vdots \\ & & & a _ {n n} \end{array} \right| = \left| \begin{array}{c c c c} a _ {1 1} & & & \\ a _ {2 1} & a _ {2 2} & & \\ \vdots & \vdots & \ddots & \\ a _ {n 1} & a _ {n 2} & \dots & a _ {n n} \end{array} \right| = a _ {1 1} a _ {2 2} \dots a _ {n n}
$$

(3) 副对角行列式: (此公式易错)

$$
\left| \begin{array}{c c c c} & & & a _ {1 n} \\ & & a _ {2, n - 1} \\ & \ddots & \\ a _ {n 1} & & \end{array} \right| = (- 1) ^ {\frac {n (n - 1)}{2}} a _ {1 n} a _ {2, n - 1} \dots a _ {n 1}
$$

（4）副对角线上（下）三角行列式：（此公式易错）

$$
\left| \begin{array}{c c c c} a _ {1 1} & \dots & \dots & a _ {1 n} \\ a _ {2 1} & \dots & a _ {2, n - 1} \\ \vdots & . & & \\ a _ {n 1} & & & \end{array} \right| = \left| \begin{array}{c c c c} & & & a _ {1 n} \\ & & a _ {2, n - 1} & a _ {2 n} \\ & \ddots & \vdots & \vdots \\ a _ {n 1} & \dots & a _ {n, n - 1} & a _ {n n} \end{array} \right| = (- 1) ^ {\frac {n (n - 1)}{2}} a _ {1 n} a _ {2, n - 1} \dots a _ {n 1}
$$

(5) n 阶范德蒙德 (Vandermonde) 行列式:

$$
D _ {n} = \left| \begin{array}{c c c c c} 1 & 1 & 1 & \dots & 1 \\ x _ {1} & x _ {2} & x _ {3} & \dots & x _ {n} \\ x _ {1} ^ {2} & x _ {2} ^ {2} & x _ {3} ^ {2} & \dots & x _ {n} ^ {2} \\ \vdots & \vdots & \vdots & & \vdots \\ x _ {1} ^ {n - 1} & x _ {2} ^ {n - 1} & x _ {3} ^ {n - 1} & \dots & x _ {n} ^ {n - 1} \end{array} \right| = \prod_ {1 \leqslant i <   j \leqslant n} \left(x _ {j} - x _ {i}\right)
$$

【例 2】设 n 阶行列式 $D = \begin{vmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 2 & \cdots & 0 \\ \vdots & \vdots & \vdots & & \vdots \\ 0 & 0 & 0 & \cdots & n - 1 \\ n & 0 & 0 & \cdots & 0 \end{vmatrix}$ ，则 $A_{k1} + A_{k2} + \cdots + A_{kn} =$ ____

【例3】计算 $D_{n} = \left| \begin{array}{cccc}1 & 1 & \dots & 1\\ x_{1} + 1 & x_{2} + 1 & \dots & x_{n} + 1\\ x_{1}^{2} + x_{1} & x_{2}^{2} + x_{2} & \dots & x_{n}^{2} + x_{n}\\ \vdots & \vdots & & \vdots \\ x_{1}^{n - 1} + x_{1}^{n - 2} & x_{2}^{n - 1} + x_{2}^{n - 2} & \dots & x_{n}^{n - 1} + x_{n}^{n - 2} \end{array} \right|.$ 

【例4】设 $f(x) = \begin{vmatrix} 1 & x & x^2 & x^3 \\ 1 & 2 & 4 & 8 \\ 1 & -1 & 1 & -1 \\ 1 & 1 & 1 & 1 \end{vmatrix}$ ，则曲线 $f(x)$ 的零点个数为（ ）. (A)0 (B)1 (C)2 (D)3

## 1.4 特殊行列式的计算

## 1.4.1 箭形/爪形行列式

【例 1】 $\begin{vmatrix}1&1&1&1\\1&2&0&0\\1&0&3&0\\1&0&0&4\end{vmatrix}=$ ____.

## 1.4.2 爪形行列式的变形

【例 2】

$$
\left| \begin{array}{c c c c} 1 & 1 & 0 & 0 \\ 1 & 2 & 1 & 0 \\ 1 & 0 & 3 & 1 \\ 1 & 0 & 0 & 4 \end{array} \right| =
$$

【例 3】 $\begin{vmatrix}1&1&1&1\\2&0&0&1\\3&0&1&0\\4&1&0&0\end{vmatrix}=$ ____.

## 1.4.3 行和相等行列式

【例 4】

$$
D _ {n} = \left| \begin{array}{c c c c c} x & a & a & \dots & a \\ a & x & a & \dots & a \\ a & a & x & \dots & a \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a & a & a & \dots & x \end{array} \right| =
$$

【例 5】

$$
\left| \begin{array}{c c c c} 1 & - 1 & 1 & a - 1 \\ 1 & - 1 & a + 1 & - 1 \\ 1 & a - 1 & 1 & - 1 \\ a + 1 & - 1 & 1 & - 1 \end{array} \right| =
$$

提问：什么是行和相等的行列式？其计算有什么规律？

总结：行列式中每一行元素的和都相等，就说这个行列式是行和相等的。行和相等的行列式可以把各列全都加到第1列，第1列各元素就有公因子，可以提出去，第1列各元素全为1，这时各行减去第1行就可以实现降阶。

## 1.4.4 行列同数行列式

【例6】

$$
D _ {n} = \left| \begin{array}{c c c c c} x & a & a & \dots & a \\ a & x & a & \dots & a \\ a & a & x & \dots & a \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ a & a & a & \dots & x \end{array} \right| =
$$

【例7】

$$
\left| \begin{array}{c c c c} 1 & - 1 & 1 & a - 1 \\ 1 & - 1 & a + 1 & - 1 \\ 1 & a - 1 & 1 & - 1 \\ a + 1 & - 1 & 1 & - 1 \end{array} \right| =
$$