# Phương pháp chứng minh bằng phản chứng

<!-- chunk:0 level:0 source:https://toanmath.com/2018/06/phuong-phap-chung-minh-bang-phan-chung.html -->
Bài viết hướng dẫn phương pháp chứng minh bằng phản chứng thông qua các bước giải cụ thể và các ví dụ minh họa có lời giải chi tiết.

Phương pháp chứng minh bằng phản chứng: Để chứng minh định lý “$\forall x \in X$, $P\left( x \right) \Rightarrow Q\left( x \right)$” (trong đó $P\left( x \right), Q\left( x \right)$ là các mệnh đề chứa biến) ta có thể sử dụng phương pháp chứng minh bằng phản chứng như sau:

Bước 1: Giả sử tồn tại ${{x}_{0}}\in X$ sao cho $P\left( {{x}_{0}} \right)$ đúng và $Q\left( {{x}_{0}} \right)$ sai.

Bước 2: Dùng suy luận và các kiến thức toán học để đi đến mâu thuẫn.

Ví dụ minh họa

<!-- chunk:1 level:3 source:https://toanmath.com/2018/06/phuong-phap-chung-minh-bang-phan-chung.html -->
## Ví dụ 1: Chứng minh rằng với mọi số tự nhiên $n$ mà ${{n}^{3}}$ chia hết cho $3$ thì $n$ chia hết cho $3$.

Giả sử $n$ không chia hết cho $3$ khi đó $n=3k+1$ hoặc $n=3k+2$, $k\in Z.$

+ Với $n=3k+1$ ta có ${{n}^{3}}={{\left( 3k+1 \right)}^{3}}$ $=27{{k}^{3}}+27{{k}^{2}}+9k+1$ không chia hết cho $3$ (mâu thuẫn).

+ Với $n=3k+2$ ta có ${{n}^{3}}={{\left( 3k+2 \right)}^{3}}$ $=27{{k}^{3}}+54{{k}^{2}}+36k+4$ không chia hết cho $3$ (mâu thuẫn).

Vậy $n$ chia hết cho $3$.

<!-- chunk:2 level:3 source:https://toanmath.com/2018/06/phuong-phap-chung-minh-bang-phan-chung.html -->
## Ví dụ 2: Chứng minh bằng phương pháp phản chứng: Nếu phương trình bậc hai $a{{x}^{2}}+bx+c=0$ $\left( a, c \ne 0 \right)$ vô nghiệm thì các hệ số $a$ và $c$ cùng dấu.

Giả sử phương trình $a{{x}^{2}}+bx+c=0$ $\left( a, c \ne 0 \right)$ vô nghiệm và các hệ số $a$, $c$ trái dấu.

Với điều kiện $a$, $c$ trái dấu, ta có $a.c<0$, suy ra $\Delta ={{b}^{2}}-4ac$ $={{b}^{2}}+4(-ac)>0$, do đó phương trình $a{{x}^{2}}+bx+c=0$ $\left( a, c \ne 0 \right)$ có hai nghiệm phân biệt, điều này mâu thuẫn với giả thiết phương trình vô nghiệm.

Vậy phương trình vô nghiệm $a{{x}^{2}}+bx+c=0$ $\left( a, c \ne 0 \right)$ thì $a$, $c$ phải cùng dấu.

<!-- chunk:3 level:3 source:https://toanmath.com/2018/06/phuong-phap-chung-minh-bang-phan-chung.html -->
## Ví dụ 3: Chứng minh rằng $\sqrt{2}$ là số vô tỉ.

Dễ dàng chứng minh được nếu ${n^2}$ là số chẵn thì $n$ là số chẵn.

Giả sử $\sqrt 2$ là số hữu tỉ, tức là $\sqrt 2 = \frac{m}{n}$, trong đó $m, n ∈ N^*$, $\left( {m,n} \right) = 1.$

Từ $\sqrt 2 = \frac{m}{n}$ $\Rightarrow {m^2} = 2{n^2}$ $\Rightarrow {m^2}$ là số chẵn.

Suy ra $m$ là số chẵn $⇒$ $m = 2k$, $k \in {N^*}.$

Từ ${m^2} = 2{n^2}$ $\Rightarrow 4{k^2} = 2{n^2}$ $\Rightarrow {n^2} = 2{k^2}$ $\Rightarrow {n^2}$ là số chẵn $⇒$ $n$ là số chẵn.

Do đó $m$ chẵn, $n$ chẵn, mâu thuẫn với $\left( m,n \right) = 1.$

Vậy $\sqrt 2$ là số vô tỉ.

<!-- chunk:4 level:3 source:https://toanmath.com/2018/06/phuong-phap-chung-minh-bang-phan-chung.html -->
## Ví dụ 4: Cho $a, b, c$ là các số dương thỏa mãn $abc = 1$. Chứng minh rằng nếu $a + b + c > \frac{1}{a} + \frac{1}{b} + \frac{1}{c}$ thì có một và chỉ một trong ba số $a, b, c$ lớn hơn $1$.

Ta có các trường hợp sau:

+ Trường hợp 1: Giả sử ba số $a, b, c$ đều lớn hơn $1$ hoặc ba số $a, b, c$ đều nhỏ hơn $1$ thì mâu thuẫn với giả thiết $abc = 1.$

+ Trường hợp 2: Giả sử hai trong ba số $a, b, c$ lớn hơn $1.$

Không mất tính tổng quát giả sử $a > 1, b > 1.$

Vì $abc = 1$ nên $c < 1$, do đó: $\left( {a – 1} \right)\left( {b – 1} \right)\left( {c – 1} \right) < 0$ $\Leftrightarrow abc + a + b + c$ $– ab – bc – ca – 1 < 0$ $\Leftrightarrow a + b + c < ab + bc + ca$ $\Leftrightarrow a + b + c < \frac{1}{a} + \frac{1}{b} + \frac{1}{c}$ (mâu thuẫn).

Vậy chỉ có một và chỉ một trong ba số $a, b, c$ lớn hơn $1$.

<!-- chunk:5 level:3 source:https://toanmath.com/2018/06/phuong-phap-chung-minh-bang-phan-chung.html -->
## Ví dụ 5: Cho các số $a, b, c$ thỏa các điều kiện:
$$
\left\{ \begin{array}{l}
a + b + c > 0\\
ab + bc + ca > 0\\
abc > 0
\end{array} \right. .
$$
 Chứng minh rằng cả ba số $a, b, c$ đều dương.

Giả sử ba số $a, b, c$ không đồng thời là số dương, vậy có ít nhất một số không dương.

Do $a, b, c$ có vai trò bình đẳng nên ta có thể giả sử: $a \le 0.$

+ Nếu $a = 0$ thì mâu thuẫn với $abc > 0.$

+ Nếu $a < 0$ thì từ $abc > 0$ $\Rightarrow bc < 0.$

Ta có $ab + bc + ca > 0$ $\Leftrightarrow a(b + c) > – bc$ $\Rightarrow a(b + c) > 0$ $\Rightarrow b + c < 0$ $\Rightarrow a + b + c < 0$ (mâu thuẫn).

Vậy cả ba số $a, b, c$ đều dương.

**Ví dụ 6**: Chứng minh rằng một tam giác có đường trung tuyến vừa là phân giác xuất phát từ một đỉnh là tam giác cân tại đỉnh đó.

<img link="data_for_rag/toan10/images/phuong-phap-chung-minh-bang-phan-chung-1.png" alt="phuong-phap-chung-minh-bang-phan-chung-1">

Giả sử tam giác $ABC$ có $AH$ vừa là đường trung tuyến vừa là đường phân giác và không cân tại $A.$

Vì $AC≠AB$, không mất tính tổng quát, ta giả sử như $AC>AB$ .

Trên $AC$ lấy $D$ sao cho $AB=AD$ .

Gọi $L$ là giao điểm của $BD$ và $AH$.

Khi đó $AB=AD$, $\widehat{BAL}=\widehat{LAD}$ và $AL$ chung nên $\Delta ABL=\Delta ADL .$

Do đó $BL=LD$ hay $L$ là trung điểm của $BD.$

Suy ra $LH$ là đường trung bình của tam giác $CBD$

$\Rightarrow LH//DC$ điều này mâu thuẫn vì $LH,DC$ cắt nhau tại $A.$

Vậy tam giác $ABC$ cân tại $A.$