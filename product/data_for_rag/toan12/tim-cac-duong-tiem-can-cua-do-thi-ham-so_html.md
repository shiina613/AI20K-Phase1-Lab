# Tìm các đường tiệm cận của đồ thị hàm số

<!-- chunk:0 level:0 source:https://toanmath.com/2018/04/tim-cac-duong-tiem-can-cua-do-thi-ham-so.html -->
Bài viết hướng dẫn tìm các đường tiệm cận của đồ thị hàm số (tiệm cận ngang, tiệm cận đứng, tiệm cận xiên) thông qua lý thuyết, các mẹo tìm nhanh tiệm cận và các ví dụ minh họa có lời giải chi tiết. Kiến thức và các ví dụ trong bài viết được tham khảo từ các tài liệu về chuyên đề hàm số được đăng tải trên TOANMATH.com.

Phương pháp
1. Tìm tiệm cận ngang, tiệm cận đứng của đồ thị hàm số $y = f(x)$
Thực hiện theo các bước sau:

+ Bước 1. Tìm tập xác định của hàm số $f(x).$

+ Bước 2. Tìm các giới hạn của $f(x)$ khi $x$ dần tới các biên của miền xác định và dựa vào định nghĩa của các đường tiệm cận để kết luận.

Chú ý:

+ Đồ thị hàm số $f$ chỉ có thể có tiệm cận ngang khi tập xác định của nó là một khoảng vô hạn hay một nửa khoảng vô hạn (nghĩa là biến $x$ có thể tiến đến $+ \infty$ hoặc  $– \infty$).

+ Đồ thị hàm số $f$ chỉ có thể có tiệm cận đứng khi tập xác định của nó có một trong các dạng sau: $(a;b)$, $[a;b)$, $(a;b]$, $(a;+∞)$, $(-∞;b)$ hoặc là hợp của các tập hợp này và tập xác định không có một trong các dạng sau: $R$, $(c;+∞)$, $(-∞;d)$, $[c;d]$.
2. Tìm tiệm cận xiên của đồ thị hàm số $y = f(x)$
Thực hiện theo các bước sau:

+ Bước 1. Tìm tập xác định của hàm số (đồ thị hàm số $f$ chỉ có thể có tiệm cận xiên nếu tập xác định của nó là là một khoảng vô hạn hay một nửa khoảng vô hạn).
+ Bước 2. Sử dụng định nghĩa về tiệm cận xiên. Hoặc sử dụng định lí sau:

Nếu $\mathop {\lim }\limits_{x \to + \infty } \frac{{f(x)}}{x} = a \ne 0$ và $\mathop {\lim }\limits_{x \to + \infty } [f(x) – ax] = b$ hoặc $\mathop {\lim }\limits_{x \to – \infty } \frac{{f(x)}}{x} = a \ne 0$ và $\mathop {\lim }\limits_{x \to – \infty } [f(x) – ax] = b$ thì đường thẳng ${\rm{y}} = {\rm{ax}} + {\rm{b}}$ là tiệm cận xiên của đồ thị hàm số $f$.

CHÚ Ý: Đối với hàm phân thức: $f\left( x \right) = \frac{{P(x)}}{{Q(x)}}$ trong đó $P(x)$, $Q(x)$ là hai đa thức của $x$ ta thường dùng phương pháp sau để tìm các đường tiệm cận của đồ thị hàm số:
a. Tiệm cận đứng

+ Nếu 
$$
\left\{ \begin{array}{l}
P({x_0}) \ne 0\\
Q({x_0}) = 0
\end{array} \right.
$$
 thì đường thẳng: $x = {x_0}$ là tiệm cận đứng của đồ thị hàm số.

b. Tiệm cận ngang
+ Nếu bậc của $P(x)$ bé hơn bậc của $Q(x)$ thì đồ thị của hàm số có tiệm cận ngang là trục hoành độ.

+ Nếu bậc của $P(x)$ bằng bậc của $Q(x)$ thì đồ thị hàm có tiệm cận ngang là đường thẳng: $y = \frac{A}{B}$ trong đó $A$, $B$ lần lượt là hệ số của số hạng có số mũ lớn nhất của $P(x)$ và $Q(x).$

+ Nếu bậc của $P(x)$ lớn hơn bậc của $Q(x)$ thì đồ thị của hàm số không có tiệm cận ngang.

c. Tiệm cận xiên
+ Nếu bậc của $P(x)$ bé hơn hay bằng bậc của $Q(x)$ hoặc lớn hơn bậc của $Q(x)$ từ hai bậc trở lên thì đồ thị hàm số không có tiệm cận xiên.

+ Nếu bậc của $P(x)$ lớn hơn bậc của $Q(x)$ một bậc và $P(x)$ không chia hết cho $Q(x)$ thì đồ thị hàm có tiệm cận xiên và ta tìm tiệm cận xiên bằng cách chia $P(x)$ cho $Q(x)$ và viết ${\rm{f}}\left( {\rm{x}} \right) = {\rm{ax}} + {\rm{b}} + \frac{{R(x)}}{{Q(x)}}$, trong đó $\mathop {\lim }\limits_{x \to + \infty } \frac{{R(x)}}{{Q(x)}} = 0$, $\mathop {\lim }\limits_{x \to – \infty } \frac{{R(x)}}{{Q(x)}} = 0$. Suy ra đường thẳng ${\rm{y}} = {\rm{ax}} + {\rm{b}}$ là tiệm cận xiên của đồ thị hàm số.

[ads]

Ví dụ minh họa
Tìm tiệm cận của hàm số:

a. $y = \frac{{2x + 1}}{{x + 1}}.$

b. $y = \frac{{2 – 4x}}{{1 – x}}.$

c. $y = 2x + 1 – \frac{1}{{x + 2}}.$

d. $y = \frac{{{x^2}}}{{1 – x}}.$

a. $y = \frac{{2x + 1}}{{x + 1}}.$

$\mathop {\lim }\limits_{x \to + \infty } y = 2$, $\mathop {\lim }\limits_{x \to – \infty } y = 2$, suy ra đường thẳng $y = 2$ là đường tiệm cận ngang của đồ thị $(C).$

$\mathop {\lim }\limits_{x \to – {1^ + }} y = – \infty$, $\mathop {\lim }\limits_{x \to – {1^ – }} y = + \infty$, suy ra đường thẳng $x = -1$ là đường tiệm cận đứng của đồ thị $(C).$

b. $y = \frac{{2 – 4x}}{{1 – x}}.$

$\mathop {\lim }\limits_{x \to + \infty } y = 4$, $\mathop {\lim }\limits_{x \to – \infty } y = 4$, suy ra đường thẳng $y = 4$ là đường tiệm cận ngang của đồ thị $(C).$

$\mathop {\lim }\limits_{x \to – {1^ + }} y = – \infty$, $\mathop {\lim }\limits_{x \to – {1^ – }} y = + \infty$, suy ra đường thẳng $x = 1$ là đường tiệm cận đứng của đồ thị $(C).$

c. $y = 2x + 1 – \frac{1}{{x + 2}}.$

$\mathop {\lim }\limits_{x \to – {2^ – }} y = + \infty$, $\mathop {\lim }\limits_{x \to – {2^ + }} y = – \infty$, suy ra đường thẳng $x = -2$ là tiệm cận đứng của $(C).$

$\mathop {\lim }\limits_{x \to – \infty } y = – \infty$, $\mathop {\lim }\limits_{x \to + \infty } y = + \infty$.

$\mathop {\lim }\limits_{x \to – \infty } [y – (2x + 1)] = 0$, $\mathop {\lim }\limits_{x \to + \infty } [y – (2x + 1)] = 0$, suy ra đường thẳng $y = 2x + 1$ là tiệm cận xiên của $(C).$

d. $y = – x – 1 + \frac{1}{{1 – x}}.$

$\mathop {\lim }\limits_{x \to {1^ – }} y = + \infty$, $\mathop {\lim }\limits_{x \to {1^ + }} y = – \infty$, suy ra đường thẳng $x = 1$ là tiệm cận đứng của $(C).$

$\mathop {\lim }\limits_{x \to – \infty } y = + \infty$, $\mathop {\lim }\limits_{x \to + \infty } y = – \infty$.

$\mathop {\lim }\limits_{x \to – \infty } [y – ( – x – 1)] = 0$, $\mathop {\lim }\limits_{x \to + \infty } [y – ( – x – 1)] = 0$, suy ra đường thẳng $y = – x – 1$ là tiệm cận xiên của $(C).$