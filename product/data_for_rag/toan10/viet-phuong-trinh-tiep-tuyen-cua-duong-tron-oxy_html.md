# Viết phương trình tiếp tuyến của đường tròn (Oxy)

<!-- chunk:0 level:0 source:https://toanmath.com/2018/04/viet-phuong-trinh-tiep-tuyen-cua-duong-tron-oxy.html -->
Bài viết hướng dẫn phương pháp viết phương trình tiếp tuyến của đường tròn thỏa mãn điều kiện cho trước trong hệ trục tọa độ Oxy, kiến thức và các ví dụ trong bài viết được tham khảo từ các tài liệu phương pháp tọa độ trong mặt phẳng được đăng tải trên TOANMATH.com.

Phương pháp
Cho đường tròn $(C)$: ${\left( {x – a} \right)^2} + {\left( {y – b} \right)^2} = {R^2}$. $(C)$ có tâm $I(a;b)$ và bán kính $R$. Ta xét các dạng toán sau:

<!-- chunk:1 level:2 source:https://toanmath.com/2018/04/viet-phuong-trinh-tiep-tuyen-cua-duong-tron-oxy.html -->
## Bài toán 1: Viết phương trình tiếp tuyến với đường tròn $(C)$ tại điểm $M\left( {{x_0};{y_0}} \right) \in \left( C \right).$

Giải: Gọi $Δ$ là tiếp tuyến với đường tròn $(C)$. Vì $Δ$ tiếp xúc với $(C)$ tại $M$ $⇒$ $Δ$ đi qua $M$ và nhận $\overrightarrow {IM} \left( {{x_0}-a;{\rm{ }}{y_0}-b} \right)$ làm vectơ pháp tuyến $⇒$ phương trình $Δ$ có dạng: $\left( {{x_0}–a} \right)\left( {x – {x_0}} \right) + \left( {{y_0}–a} \right)\left( {y – {y_0}} \right) = 0$ $(1).$

Chú ý:

+ Phương trình $(1)$ có thể biến đổi về dạng sau: $\left( {{x_0}–a} \right)\left( {x – a} \right) + \left( {{y_0}–a} \right)\left( {y – b} \right) = {R^2}$ $(1a).$

+ Nếu phương trình đường tròn cho ở dạng: ${x^2} + {y^2} – 2ax – 2by + c = 0$ thì tiếp tuyến của đường tròn tại điểm $M\left( {{x_0},{y_0}} \right)$ có dạng: $x{x_0} + y{y_0}–\left( {x + {x_0}} \right)a – \left( {y + {y_0}} \right)b + c = 0$ $(1b)$ (Phương trình này được suy ra trực tiếp từ $(1a)$).

Cách thành lập phương trình tiếp tuyến ở dạng $(1a)$ và $(1b)$ gọi là “phương pháp phân đôi toạ độ”.

<!-- chunk:2 level:2 source:https://toanmath.com/2018/04/viet-phuong-trinh-tiep-tuyen-cua-duong-tron-oxy.html -->
## Bài toán 2: Viết phương trình tiếp tuyến với đường tròn kẻ từ một điểm $M\left( {{x_0};{y_0}} \right)$ không thuộc đường tròn.

Bài toán này có hai cách giải như sau:

Cách 1:

+ Xét đường thẳng $Δ$ đi qua $M$ và vuông góc với $Ox$. Khi đó $Δ$ có phương trình là $x = {x_0}.$ $Δ$ là tiếp tuyến của đường tròn $\Leftrightarrow d(I;\Delta ) = R.$ Từ đẳng thức này sẽ suy ra được $Δ$ có phải là tiếp tuyến của đường tròn hay không.

+ Xét đường thẳng $Δ$ đi qua $M$ và có hệ số góc là $k$. Phương trình của $Δ$ có dạng: $y = k\left( {x – {x_0}} \right) + {y_0}.$ $Δ$ tiếp xúc với $(C)$ $\Leftrightarrow d(I;\Delta ) = R.$ Giải điều kiện này ta sẽ tìm được $k$.

Chú ý: Để chứng minh một điểm $M$ nằm ngoài đường tròn ta làm như sau:

– Tính $IM$.

– So sánh $IM$ với $R$:

+ Nếu $IM > R$ thì $M$ nằm ngoài đường tròn.

+ Nếu $IM < R$ thì $M$ nằm trong đường tròn.

+ Nếu $IM = R$ thì $M$ nằm trên đường tròn.

Cách 2:

+ Đường thẳng $Δ$ đi qua $M$ có phương trình: $a\left( {x – {x_0}} \right) + b\left( {y – {y_0}} \right) = 0$, trong đó ${a^2} + {b^2} \ne 0.$

+ $Δ$ là tiếp tuyến với đường tròn $(C)$ $\Leftrightarrow d(I;\Delta ) = R$ $(*).$

+ Từ điều kiện $(*)$, tìm mối liên hệ giữa $a$ và $b$. Vì $a$ và $b$ không đồng thời bằng $0$ nên có thể chọn $a$ một giá trị thích hợp rồi suy ra $b$ hoặc ngược lại.

<!-- chunk:3 level:2 source:https://toanmath.com/2018/04/viet-phuong-trinh-tiep-tuyen-cua-duong-tron-oxy.html -->
## Bài toán 3: Lập phương trình tiếp tuyến với đường tròn biết tiếp tuyến có hệ số góc là $k$.

**Giải:**

+ Phương trình đường thẳng $Δ$ có hệ số góc $k$ có dạng: $y = kx + m.$

+ $Δ$ tiếp xúc với $(C)$ $\Leftrightarrow d(I;\Delta ){\rm{ }} = {\rm{ }}R$. Giải điều kiện này ta sẽ tìm được $m$.

Chú ý:

+ Nếu tiếp tuyến $Δ$ song song với đường thẳng: $ax + by + c = 0$ thì phương trình $Δ$ sẽ có dạng: $ax + by + c’ = 0 (c’ ≠ c).$

+ Nếu tiếp tuyến $Δ$ vuông góc với đường thẳng: $ax + by + c = 0$ thì phương trình $Δ$ sẽ có dạng: $-bx + ay + c’ = 0 (c’ ≠ c).$

Ví dụ minh họa

<!-- chunk:4 level:3 source:https://toanmath.com/2018/04/viet-phuong-trinh-tiep-tuyen-cua-duong-tron-oxy.html -->
## Ví dụ 1: Cho đường tròn $(C)$ có phương trình: ${x^2} + {y^2} – 6x + 2y + 6 = 0$ và điểm $A(1;3)$.

a. Chứng minh rằng điểm $A$ ở ngoài đường tròn.

b. Viết phương trình tiếp tuyến của $(C)$ kẻ từ $A$.

Đường tròn $(C)$ có tâm $I(3;-1)$ bán kính $R = 2$.

a. Ta có: $IA = 2\sqrt 5 > R$ ⇒ $A$ nằm ngoài đường tròn $(C)$.

b. Ta giải bài toán này theo hai cách:

Cách 1:  Phương trình đường thẳng đi qua $A$ có vectơ pháp tuyến là $(a;b)$ có dạng:

$a\left( {x–2} \right) + b\left( {y–6} \right) = 0$ $({a^2} + {b^2} \ne 0).$

Đường thẳng này là tiếp tuyến của đường tròn $\Leftrightarrow d\left( {I,d} \right) = R$

$\Leftrightarrow \frac{{\left| {a(3 – 1) + b( – 1 – 3)} \right|}}{{\sqrt {{a^2} + {b^2}} }} = 2$ $\Leftrightarrow {\left( {a – 2b} \right)^2} = \left( {{a^2} + {b^2}} \right)$ $\Leftrightarrow 3{b^2} – 4ab = 0$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
b = 0\\
b = \frac{4}{3}a
\end{array} \right.
$$

+ Nếu $b = 0$, vì $a ≠ 0$ chọn $a = 1$ $⇒$ phương trình tiếp tuyến có dạng: $x = 1$.

+ Nếu $b = \frac{4}{3}a.$ Chọn $a = 3, b = 4$ thì phương trình tiếp tuyến có dạng: $3x – 4y – 15 = 0.$

Vậy qua $A$ kẻ được hai tiếp tuyến với $(C)$ là: $x = 1$ và $3x – 4y – 15 = 0.$

Cách 2:

+ Xét $Δ$ đi qua $A$ và vuông góc với $Ox$ $⇒$ phương trình $Δ:$ $x = 1$ hay $x – 1 = 0.$

$Δ$ là tiếp tuyến của $(C)$ $\Leftrightarrow d(I;\Delta ) = R$ $\Leftrightarrow \frac{{\left| {3 – 1} \right|}}{{\sqrt 1 }} = 2.$ Đẳng thức này đúng nên $x = 1$ là tiếp tuyến của $(C).$

+ Xét $Δ$ đi qua $A$ và có hệ số góc là $k$. Phương trình của $Δ$ là: $y = k(x – 1) + 3$ hay $kx – y + 3 – k = 0.$

$Δ$ tiếp xúc với $(C)$ $\Leftrightarrow d(I;\Delta ) = R$ $\Leftrightarrow \frac{{\left| {3k + 1 + 3 – k} \right|}}{{\sqrt {{k^2} + 1} }} = 2.$

${\left( {k + 2} \right)^2} = {k^2} + 1 \Leftrightarrow k = – \frac{3}{4}$ ⇒ ta được tiếp tuyến: $y = – \frac{3}{4}\left( {x–1} \right) + 3$ $\Leftrightarrow 3x + 4y–15 = 0.$

Nhận xét: Trong cách giải 2, ta phải xét hai trường hợp nhưng lời giải của mỗi trường hợp lại khá ngắn gọn và đơn giản. Phù hợp với đối tượng học sinh mà kỹ năng tính toán còn hạn chế. Một sai lầm mà học sinh thường mắc phải khi giải theo cách này đó là không xét trường hợp thứ nhất tức là tiếp tuyến vuông góc với $Ox$ (đường thẳng không có hệ số góc) và do đó bài toán sẽ mất nghiệm.

<!-- chunk:5 level:3 source:https://toanmath.com/2018/04/viet-phuong-trinh-tiep-tuyen-cua-duong-tron-oxy.html -->
## Ví dụ 2: Cho đường tròn có phương trình là: ${x^2} + {y^2} + 4x + 4y – 17 = 0.$ Viết phương trình tiếp tuyến $d$ của đường tròn trong các trường hợp sau:

a. Điểm tiếp xúc là $M(2;1).$

b. $d$ đi qua $A(3;6).$

c. $d$ song song với đường thẳng $3x – 4y – 2008 = 0.$

Đường tròn này có tâm $I(-2;-2)$, bán kính $R = 5.$

a. Đây là bài toán tiếp tuyến thứ nhất.

Theo phương pháp phân đôi toạ độ $⇒$ Phương trình tiếp tuyến với đường tròn tại $M(2;1)$ là:

$2x +1.y + 2(x + 2) + 2(y + 1) – 17 = 0$

$⇔ 4x + 3y – 11 = 0.$

b. Đây là bài toán tiếp tuyến thứ hai.

Phương trình đường thẳng đi qua $A$ có vectơ pháp tuyến là $(a;b)$ có dạng:

$a(x – 2) + b(y – 6) = 0.$

Đường thẳng này là tiếp tuyến của đường tròn $⇔ d(I,d) = R$

$\Leftrightarrow \frac{{\left| {a( – 2 – 3) + b( – 2 – 6)} \right|}}{{\sqrt {{a^2} + {b^2}} }} = 5$

$\Leftrightarrow {\left( {5a + 8b} \right)^2} = 25\left( {{a^2} + {b^2}} \right)$ $\Leftrightarrow 39{b^2} + 80ab = 0.$

+ Nếu $b = 0$, vì $a ≠ 0$ chọn $a = 1$ $⇒$ phương trình tiếp tuyến có dạng: $x = 2.$

+ Nếu $b \ne 0 \Rightarrow a{\rm{ }} = \frac{{ – 39}}{{80}}b.$ Chọn $a = -39, b = 80$, phương trình tiếp tuyến có dạng: $-39x + 80y – 402 = 0.$

Vậy có hai tiếp tuyến thoả mãn đầu bài.

c. Đây là bài toán tiếp tuyến thứ ba.

Phương trình đường thẳng song song với đường thẳng $3x – 4y – 2008 = 0$ có dạng: $3x – 4y + c = 0.$

Đường thẳng này là tiếp tuyến với đường tròn $\Leftrightarrow d(I;{d_3}) = R$ $\Leftrightarrow \frac{{\left| {3.( – 2) – 4( – 2) + c} \right|}}{{\sqrt {{3^2} + {4^2}} }} = 5$ $\Leftrightarrow \left| {2 + c} \right| = 25$ $⇒$ $c = 23$ hoặc $c = -27.$

Vậy có hai tiếp tuyến thoả mãn là: $3x – 4y + 23 = 0$ hoặc $3x – 4y – 27 = 0.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/04/viet-phuong-trinh-tiep-tuyen-cua-duong-tron-oxy.html -->
## Ví dụ 3: Cho đường tròn ${x^2} + {y^2} – 2x – 6y + 6 = 0$ và điểm $M(2;4).$

a. Viết phương trình đường thẳng đi qua $M$ cắt đường tròn tại hai điểm $A, B$ sao cho $M$ là trung điểm của đoạn thẳng $AB.$

b. Viết phương trình tiếp tuyến của đường tròn có hệ số góc $k = -1.$

Đường tròn này có tâm $I(1;3)$ và bán kính $R = 2.$

a. Ta có: $IM = \sqrt 2 < 2 = R$ $⇒$ $M$ nằm trong đường tròn. Vậy mọi đường thẳng đi qua $M$ đều cắt đường tròn tại hai điểm phân biệt.

Đường thẳng $Δ$ đi qua $M$ cắt đường tròn tại hai điểm $A$ và $B$ sao cho $M$ là trung điểm của $AB$ $⇒$ $IM ⊥ AB$ ⇒ $Δ$ nhận $\overrightarrow {IM} (1;1)$ làm vectơ pháp tuyến $⇒$ phương trình của $Δ$: $x – 2 + y – 4 = 0$ ⇔ $x + y – 6 = 0.$

b. Phương trình của $Δ$ có hệ số góc là $k = -1$: $y = -x + m$ hay $x + y – m = 0$

$Δ$ tiếp xúc với $(C)$ $\Leftrightarrow d(I;\Delta ) = R$ $\Leftrightarrow \frac{{\left| {1 + 3 – m} \right|}}{{\sqrt {1 + 1} }} = 2$

${\left( {4 – m} \right)^2} = {\rm{ }}8$ 
$$
\Leftrightarrow \left[ \begin{array}{l}
m = 4 – 2\sqrt 2 \\
m = 4 + 2\sqrt 2
\end{array} \right.
$$

Vậy có hai tiếp tuyến thoả mãn đề bài là: $x + y – 4 + 2\sqrt 2 = 0$ và $x + y – 4 – 2\sqrt 2 = 0.$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/04/viet-phuong-trinh-tiep-tuyen-cua-duong-tron-oxy.html -->
## Ví dụ 4: Cho đường tròn $(C):{x^2} + {y^2} + 2x – 4y – 4 = 0$ và điểm $A(2;5).$ Lập phương trình tiếp tuyến kẻ từ $A$ tới đường tròn. Giả sử tiếp tuyến này tiếp xúc với đường tròn tại hai điểm $M, N$. Hãy tính độ dài $MN.$

Qua $A$ ta kẻ được hai tiếp tuyến với đường tròn là: $x = 2$ và $y = 5$.

Toạ độ của điểm $M$ là nghiệm của hệ phương trình:

$$
\left\{ \begin{array}{l}
x = 2\\
{x^2} + {y^2} – 2x – 6y + 6 = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x = 2\\
y = 2
\end{array} \right.
$$
 $⇒ M(2;2).$

Toạ độ của điểm $N$ là nghiệm của hệ phương trình:

$$
\left\{ \begin{array}{l}
y = 5\\
{x^2} + {y^2} – 2x – 6y + 6 = 0
\end{array} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{array}{l}
x = – 1\\
y = 5
\end{array} \right.
$$
 $⇒ N(-1;5).$

Suy ra: $MN = \sqrt {{{\left( { – 1 – 2} \right)}^2} + {{(5 – 2)}^2}} = 3\sqrt 2 .$

<!-- chunk:8 level:3 source:https://toanmath.com/2018/04/viet-phuong-trinh-tiep-tuyen-cua-duong-tron-oxy.html -->
## Ví dụ 5: Cho $(C):{x^2} + {y^2} – 2x + 2y – 3 = 0.$ Viết phương trình tiếp tuyến của $(C)$ biết tiếp tuyến cắt tia $Ox, Oy$ lần lượt tại $A$ và $B$ sao cho $ΔABC$ có diện tích bằng $4.$

$(C)$ có tâm $I(1;-1)$ và bán kính $R = \sqrt 5 .$

Giả sử $A(a;0), B(0;b)$ trong đó $a > 0$ và $b > 0.$

Phương trình đường thẳng $AB$ có dạng: $\frac{x}{a} + \frac{y}{b} = 1$ $\Leftrightarrow bx + ay – ab = 0.$

${S_{AOB}} = 4$ $\Rightarrow \frac{1}{2}\left| {ab} \right| = 4 \Rightarrow ab = 8.$

$AB$ tiếp xúc với $(C)$ $\Rightarrow d\left( {I,AB} \right) = R$ $\Leftrightarrow \frac{{\left| {b – a – ab} \right|}}{{\sqrt {{a^2} + {b^2}} }} = \sqrt 5$ $\Rightarrow b–a = – 2$ 
$$
\Rightarrow \left\{ \begin{array}{l}
a = 4\\
b = 2
\end{array} \right.
$$

Vậy phương trình $AB: x + 2y – 4 = 0.$