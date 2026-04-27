# Mặt cầu trong không gian

<!-- chunk:0 level:0 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
TOANMATH.com giới thiệu đến đọc giả bài viết **mặt cầu trong không gian** thuộc chương trình Hình học 12 chương 3: phương pháp tọa độ trong không gian Oxyz. Bài viết trình bày các vấn đề: lập phương trình mặt cầu, vị trí tương đối giữa mặt cầu và mặt phẳng, vị trí tương đối giữa mặt cầu và đường thẳng.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## A. PHƯƠNG PHÁP GIẢI TOÁN
1) Lập phương trình mặt cầu:

• Để lập phương trình mặt cầu ta cần tìm tâm $I(a;b;c)$ và bán kính $R.$ Khi đó phương trình mặt cầu có dạng:

${{(x-a)}^{2}}+{{(y-b)}^{2}}+{{(z-c)}^{2}}={{R}^{2}}.$

• Ngoài ra để lập phương trình mặt cầu ta có thể tìm các hệ số $a$, $b$, $c$, $d$ trong phương trình: ${{x}^{2}}+{{y}^{2}}+{{z}^{2}}-2ax-2by-2cz+d=0$, với tâm $I(a;b;c)$, bán kính ${{R}^{2}}={{a}^{2}}+{{b}^{2}}+{{c}^{2}}-d>0.$

• Một mặt cầu được hoàn toàn xác định khi biết tâm và bán kính hoặc biết đường kính.

2) Vị trí tương đối giữa mặt cầu và mặt phẳng:

Cho mặt cầu tâm $I$, bán kính $R$ và mặt phẳng $(\alpha )$, $h=d\left( I,(\alpha ) \right)$, $H$ là hình chiếu của $I$ lên mặt phẳng $(\alpha ).$

• $h>R$ thì $(\alpha )$ và mặt cầu $(I)$ không giao nhau.

• $h=R$ thì $(\alpha )$ và mặt cầu $(I)$ tiếp xúc nhau tại $H.$

• $h<R$ thì $(\alpha )$ và mặt cầu $(I)$ cắt nhau theo giao tuyến là đường tròn tâm $H$, bán kính $r=\sqrt{{{R}^{2}}-{{h}^{2}}}.$

3) Vị trí tương đối giữa mặt cầu và đường thẳng:

Cho mặt cầu tâm $I$, bán kính $R$ và đường thẳng $\Delta$, $h=d\left( I,\Delta \right)$, $H$ là hình chiếu của $I$ lên mặt phẳng $\Delta .$

• $h>R$ thì $\Delta$ và mặt cầu $(I)$ không giao nhau.

• $h=R$ thì $\Delta$ và mặt cầu $(I)$ tiếp xúc nhau tại $H.$ Hay $\Delta$ là tiếp tuyến của mặt cầu $(I).$

• $h<R$ thì $\Delta$ và mặt cầu $(I)$ cắt nhau tại hai điểm phân biệt $A$, $B$ và $H$ là trung điểm của dây cung $AB$, do đó: ${{R}^{2}}=\frac{A{{B}^{2}}}{4}+{{h}^{2}}.$

<!-- chunk:2 level:3 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## Ví dụ 1. Trong không gian với hệ tọa độ $Oxyz$, cho điểm $A(0;0;-2)$ và đường thẳng $\Delta :\frac{x+2}{2}=\frac{y-2}{3}=\frac{z+3}{2}.$ Tính khoảng cách từ $A$ đến $\Delta .$ Viết phương trình mặt cầu tâm $A$, cắt $\Delta$ tại hai điểm $B$ và $C$ sao cho $BC=8.$

Đường thẳng $\Delta$ qua $M\left( -2;2;-3 \right)$ và có $\overrightarrow{u}=\left( 2;3;2 \right)$ là VTCP.

$d\left( A,\Delta \right)=\frac{\left| \left[ \overrightarrow{AM},\overrightarrow{u} \right] \right|}{\left| \overrightarrow{u} \right|}=3.$

Gọi $H$ là hình chiếu của $A$ lên $\Delta$ thì $AH=3$ và $H$ là trung điểm của $BC$ nên$BH=4.$ Vậy bán kính mặt cầu là $AB=\sqrt{A{{H}^{2}}+B{{H}^{2}}}=5.$

Nên phương trình mặt cầu là ${{x}^{2}}+{{y}^{2}}+{{\left( z+2 \right)}^{2}}=25.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## Ví dụ 2. Trong không gian với hệ tọa độ $Oxyz$, cho đường thẳng $\Delta$ có phương trình:$\frac{x-1}{2}=\frac{y-3}{4}=\frac{z}{1}$ và mặt phẳng $(P):2x-y+2z=0.$ Viết phương trình mặt cầu có tâm thuộc đường thẳng $\Delta$, bán kính bằng $1$ và tiếp xúc với mặt phẳng $(P).$

Gọi $(S)$ là mặt cầu cần tìm, $I$ là tâm.

Phương trình tham số đường thẳng 
$$
\Delta :\left\{ \begin{align}
& x=1+2t \\
& y=3+4t \\
& z=t \\
\end{align} \right. .
$$

Vì $I\in \Delta$ $\Rightarrow I\left( 1+2t;3+4t;t \right).$

Ta có $(P)$ tiếp xúc với $(S)$ nên: $d(I,(P))=1$ $\Leftrightarrow \frac{\left| 2(1+2t)-(3+4t)+2t \right|}{3}=1$ $\Leftrightarrow t=2$, $t=-1.$

• $t=2$ $\Rightarrow I(5;11;2)$ $\Rightarrow$ phương trình mặt cầu $(S):$ ${{(x-5)}^{2}}+{{(y-11)}^{2}}+{{(z-2)}^{2}}=1.$

• $t=-1$ $\Rightarrow I(-1;-1;-1)$, suy ra phương trình mặt cầu $(S):$ ${{(x+1)}^{2}}+{{(y+1)}^{2}}+{{(z+1)}^{2}}=1.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## Ví dụ 3. Trong không gian với hệ tọa độ Đề các vuông góc $Oxyz$ cho $I(1;2;-2)$ và mặt phẳng $\left( P \right):2x+2y+z+5=0.$

1. Lập phương trình mặt cầu $(S)$ tâm $I$ sao cho giao của $(S)$ với mặt phẳng $(P)$ là đường tròn $(C)$ có chu vi bằng $8\pi .$

2. Chứng minh rằng mặt cầu $(S)$ nói trong phần 1 tiếp xúc với đường thẳng $\Delta :2x-2=y+3=z.$

3. Lập phương trình mặt phẳng $(Q)$ chứa đường thẳng $\Delta$ và tiếp xúc với $(S).$

1. Gọi $R$, $r$ lần lượt là bán kính của mặt cầu $(S)$ và đường tròn $(C).$

Ta có: $2\pi r=8\pi$ $\Rightarrow r=4$ và $d(I,(P))=3$ nên $R=\sqrt{{{r}^{2}}+{{d}^{2}}(I,(P))}=5.$

Vậy phương trình mặt cầu $(S):{{(x-1)}^{2}}+{{(y-2)}^{2}}+{{(z+2)}^{2}}=25.$

2. Đường thẳng $\Delta$ có $\overrightarrow{{{u}_{\Delta }}}=(1;2;2)$ là VTCP và đi qua $A(1;-3;0).$

Suy ra $\overrightarrow{AI}=(0;5;-2)$ $\Rightarrow [\overrightarrow{{{u}_{\Delta }}},\overrightarrow{AI}]=(-14;2;5)$ $\Rightarrow d(I,\Delta )=\frac{\left| [\overrightarrow{{{u}_{\Delta }}},\overrightarrow{AI}] \right|}{\left| \overrightarrow{{{u}_{\Delta }}} \right|}=5.$

Vậy đường thẳng $\Delta$ tiếp xúc với mặt cầu $(S).$

Cách khác:

Phương trình tham số của 
$$
\Delta :\left\{ \begin{align}
& x=1+t \\
& y=-3+2t \\
& z=2t \\
\end{align} \right.
$$
, thay vào phương trình mặt cầu $(S)$, ta được: ${{t}^{2}}+{{(2t-5)}^{2}}+{{(2t+2)}^{2}}=25$ $\Leftrightarrow {{(3t-2)}^{2}}=0$ $\Leftrightarrow t=\frac{2}{3}.$

Suy ra mặt cầu $(S)$ và $\Delta$ giao nhau tại một điểm $M(\frac{5}{3};-\frac{5}{3};\frac{4}{3}).$

Vậy đường thẳng $\Delta$ tiếp xúc với mặt cầu $(S)$ tại $M.$

3. Vì mặt phẳng $(Q)$ chứa $\Delta$ và tiếp xúc với mặt cầu $(S)$ nên $M$ là tiếp điểm của mặt phẳng $(Q)$ và mặt cầu $(S).$

Do đó $(Q)$ là mặt phẳng đi qua $M$ và nhận $\overrightarrow{IM}\left( \frac{2}{3};-\frac{11}{3};\frac{10}{3} \right)$ làm VTPT.

Vậy phương trình mặt phẳng $(Q):2x-11y+10z-35=0.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## Ví dụ 4. Trong không gian với hệ tọa độ $Oxyz:$

1. Lập phương trình mặt cầu $(S)$ đi qua điểm $M(1;-5;2)$ và qua đường tròn $(C)$ là giao của mặt phẳng $(\alpha ):2x+2y-z+9=0$ và mặt cầu $(S’):{{x}^{2}}+{{y}^{2}}+{{z}^{2}}+2x-4y-4z-40=0.$

2. Viết phương trình mặt phẳng $(P)$ chứa 
$$
d:\left\{ \begin{align}
& x=t \\
& y=-2+t \\
& z=-6+2t \\
\end{align} \right.
$$
 sao cho giao tuyến của mặt phẳng $(P)$ và mặt cầu $(S):{{x}^{2}}+{{y}^{2}}+{{z}^{2}}+2x-2y+2z-1=0$ là đường tròn có bán kính $r=1.$

1. Cách 1.

Mặt cầu $(S’)$ có tâm $I'(-1;2;2)$, $R’=7$, $d(I’,(\alpha ))=\frac{\left| -2+4-2+9 \right|}{\sqrt{{{2}^{2}}+{{2}^{2}}+{{(-1)}^{2}}}}=3<R’$ nên đường tròn $(C)$ tồn tại và có bán kính $r=2\sqrt{10}.$

Gọi $H$ là tâm của $(C).$

Ta có $I’H\bot (\alpha )$ 
$$
\Rightarrow I’H:\left\{ \begin{align}
& x=-1+2t \\
& y=2+2t \\
& z=2-t \\
\end{align} \right. .
$$

Suy ra tọa độ của $H$ là nghiệm của hệ: 
$$
\left\{ \begin{align}
& x=-1+2t \\
& y=2+2t \\
& z=2-t \\
& 2x+2y-z+9=0 \\
\end{align} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{align}
& x=-3 \\
& y=0 \\
& z=3 \\
\end{align} \right.
$$
 $\Rightarrow H(-3;0;3).$

Gọi $d$ là đường thẳng đi qua tâm $H$ và vuông góc với $(\alpha )$, suy ra phương trình của 
$$
d:\left\{ \begin{align}
& x=-3+2t \\
& y=2t \\
& z=3-t \\
\end{align} \right. .
$$

Gọi $I$ là tâm của mặt cầu $(S)$, vì $(S)$ đi qua đường tròn $(C)$ nên $I\in d.$

Suy ra $I(-3+2t;2t;3-t)$ $\Rightarrow \overrightarrow{MI}=(2t-4;2t+5;1-t)$, $d(I,(\alpha ))=\frac{\left| 9t \right|}{3}=3\left| t \right|.$

Mặt khác, ta có: $I{{M}^{2}}={{r}^{2}}+{{d}^{2}}(I,(\alpha ))$ $\Leftrightarrow {{(2t-4)}^{2}}+{{(2t+5)}^{2}}+{{(1-t)}^{2}}=40+9{{t}^{2}}$ $\Leftrightarrow t=-1$ $\Rightarrow I(-5;-2;4)$, $R=IM=7.$

Vậy phương trình $(S):{{(x+5)}^{2}}+{{(y+2)}^{2}}+{{(z-4)}^{2}}=49.$

Cách 2.

Vì mặt cầu $(S)$ đi qua đường tròn $(C)$ nên phương trình $(S)$ có dạng:

${{x}^{2}}+{{y}^{2}}+{{z}^{2}}+2x-4y-4z-40$ $+\lambda (2x+2y-z+9)=0$ $\Leftrightarrow {{x}^{2}}+{{y}^{2}}+{{z}^{2}}$ $+(2+2\lambda )x-(4-2\lambda )y-(4+\lambda )z-40+9\lambda =0.$

Vì $M(1;-5;2)\in (S)$ $\Rightarrow 44-10\lambda -40+9\lambda =0$ $\Leftrightarrow \lambda =4.$

Vậy phương trình mặt cầu $(S) :$ ${{x}^{2}}+{{y}^{2}}+{{z}^{2}}+10x+4y-8z-4=0.$

2. Đường thẳng $d$ đi qua $A(0;-2;-6)$ và có $\overrightarrow{u}=(1;1;2)$ là VTCP.

Phương trình của $(P)$ có dạng: $ax+b(y+2)+c(z+6)=0.$

Hay $ax+by+cz+2b+6c=0.$

Trong đó ${{a}^{2}}+{{b}^{2}}+{{c}^{2}}\ne 0$ và $a+b+2c=0$ $\Rightarrow a=-b-2c.$

Mặt cầu $(S)$ có tâm $I(-1;1;-1)$, bán kính $R=2.$

Theo giả thiết, ta suy ra $d(I,(P))=\sqrt{{{R}^{2}}-{{r}^{2}}}=\sqrt{3}.$

Do đó: $\frac{\left| -a+3b+5c \right|}{\sqrt{{{a}^{2}}+{{b}^{2}}+{{c}^{2}}}}=\sqrt{3}$ $\Leftrightarrow \left| 4b+7c \right|=\sqrt{3}.\sqrt{{{(b+2c)}^{2}}+{{b}^{2}}+{{c}^{2}}}$ $\Leftrightarrow {{(4b+7c)}^{2}}=3(2{{b}^{2}}+4bc+5{{c}^{2}})$ $\Leftrightarrow 5{{b}^{2}}+22bc+17{{c}^{2}}=0$ $\Leftrightarrow b=-c$, $b=-\frac{17}{5}c.$

• $b=-c$ ta chọn $c=-1$ $\Rightarrow b=1$ $\Rightarrow a=1$ $\Rightarrow (P):x+y-z-4=0.$

• $b=-\frac{17}{5}c$ ta chọn $c=5$ $\Rightarrow b=-17$ $\Rightarrow a=7$ $\Rightarrow (P):7x-17y+5z-4=0.$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## Ví dụ 5. Lập phương trình mặt phẳng $(P)$ biết:

1. $(P)$ chứa hai đường thẳng cắt nhau có phương trình: ${{\Delta }_{1}}:\frac{x}{1}=\frac{y+1}{1}=\frac{z+1}{1}$, ${{\Delta }_{2}}:\frac{x+2}{2}=\frac{y-2}{-3}=\frac{z}{-1}.$

2. $(P)$ chứa hai đường thẳng song song có phương trình: ${{\Delta }_{2}}:\frac{x+2}{2}=\frac{y-2}{-3}=\frac{z}{-1}$, ${{\Delta }_{3}}:\frac{x+2}{-2}=\frac{y-1}{3}=\frac{z-3}{1}.$

3. $(P)$ chứa đường thẳng ${{\Delta }_{1}}$ và tiếp xúc với mặt cầu có phương trình: $(S):{{x}^{2}}+{{y}^{2}}+{{z}^{2}}-8x+2y+4z+7=0.$

4. $(P)$ chứa đường thẳng ${{\Delta }_{3}}$ và cắt mặt cầu $(S)$ theo một đường tròn có bán kính lớn nhất.

5. $(P)$ chứa đường thẳng ${{\Delta }_{2}}$ và cắt mặt cầu $(S)$ theo một đường tròn có bán kính bằng $\frac{\sqrt{210}}{6}.$

1. Đường thẳng ${{\Delta }_{1}}$ qua ${{M}_{1}}(0;-1;-1)$ và ${{\vec{u}}_{{{\Delta }_{1}}}}(1;1;1).$

Đường thẳng ${{\Delta }_{2}}$ qua ${{M}_{2}}(-2;2;0)$ và ${{\vec{u}}_{{{\Delta }_{2}}}}(2;-3;-1).$

Cặp véc tơ chỉ phương của $(P)$ là ${{\vec{u}}_{{{\Delta }_{1}}}}(1;1;1)$ và ${{\vec{u}}_{{{\Delta }_{2}}}}(2;-3;-1)$ nên một véc tơ pháp tuyến của $(P)$ là ${{\vec{n}}_{(P)}}=\left[ {{{\vec{u}}}_{{{\Delta }_{1}}}};{{{\vec{u}}}_{{{\Delta }_{2}}}} \right]=(2;3;-5).$

Phương trình mặt phẳng $(P)$ chứa hai đường thẳng ${{\Delta }_{1}}$ và ${{\Delta }_{2}}$ là $2(x-0)+3(y+1)-5(z+1)=0$ $\Leftrightarrow 2x+3y-5z-2=0.$

2. Đường thẳng ${{\Delta }_{3}}$ qua ${{M}_{3}}(-2;1;3)$ và ${{\vec{u}}_{{{\Delta }_{3}}}}(-2;3;1).$

Cặp véc tơ chỉ phương của $(P)$ là ${{\vec{u}}_{{{\Delta }_{2}}}}(2;-3;-1)$ và $\overrightarrow{{{M}_{2}}{{M}_{3}}}(0;-1;3)$ nên một véc tơ pháp tuyến của $(P)$ là ${{\vec{n}}_{(P)}}=\left[ {{{\vec{u}}}_{{{\Delta }_{2}}}};\overrightarrow{{{M}_{2}}{{M}_{3}}} \right]=-2(5;3;1).$

Phương trình mặt phẳng $(P)$ chứa hai đường thẳng ${{\Delta }_{2}}$ và ${{\Delta }_{3}}$ là $5(x+2)+3(y-1)+1(z-3)=0$ $\Leftrightarrow 5x+3y+z+4=0.$

3. Vì $(P)$ chứa đường thẳng ${{\Delta }_{1}}$ nên $(P)$ đi qua hai điểm thuộc ${{\Delta }_{1}}$ là điểm ${{M}_{1}}(0;-1;-1)$ và ${{N}_{1}}(1;0;0).$

Phương trình mặt phẳng $(P)$ qua ${{M}_{1}}$ có dạng

$a(x-0)+b(y+1)+c(z+1)=0$, ${{a}^{2}}+{{b}^{2}}+{{c}^{2}}>0.$

Vì $(P)$ qua ${{N}_{1}}$ nên $c=-b-a.$

Mặt cầu $(S)$ có tâm $I(4;-1;-2)$ và bán kính $R=\sqrt{14}.$

$(P)$ tiếp xúc với $(S)$ khi và chỉ khi $d(I;(P))=R$, hay $\frac{{\left| {4a + b.0 + ( – b – a).( – 1)} \right|}}{{\sqrt {{a^2} + {b^2} + {{( – b – a)}^2}} }} = \sqrt {14}$ $\Leftrightarrow \left| {5a + b} \right| = \sqrt {14(2{a^2} + 2ab + 2{b^2})}$ $\Leftrightarrow {a^2} + 6ab + 9{b^2} = 0$ $\Leftrightarrow a = – 3b$

Chọn $b=-1$ thì $a=3$, $c=-2$ nên phương trình mặt phẳng cần tìm là $(P):3x-y-2z-3=0.$

4. Đường tròn giao tuyến có bán kính lớn nhất khi và chỉ khi đường tròn đó qua tâm mặt cầu. Tức là mặt phẳng $(P)$ chứa ${{\Delta }_{3}}$ và đi qua tâm $I(4;-1;-2).$ Ta có ${{\vec{u}}_{{{\Delta }_{3}}}}(-2;3;1)$ và $\overrightarrow{IM_{3}^{{}}}(-6;2;5)$ nên một véc tơ pháp tuyến của $(P)$ là ${{\vec{n}}_{(P)}}=\left[ {{{\vec{u}}}_{{{\Delta }_{3}}}};\overrightarrow{I{{M}_{3}}} \right]=(13;4;14).$

Phương trình mặt phẳng cần tìm là $(P):13x+4y+14z-20=0.$

5. Vì $(P)$ chứa đường thẳng ${{\Delta }_{2}}$ nên $(P)$ đi qua hai điểm thuộc ${{\Delta }_{2}}$ là điểm ${{M}_{2}}(-2;2;0)$ và ${{N}_{2}}(0;-1;-1).$

Phương trình mặt phẳng $(P)$ qua ${{M}_{1}}$ có dạng $a(x+2)+b(y-2)+c(z-0)=0$, ${{a}^{2}}+{{b}^{2}}+{{c}^{2}}>0.$

Vì $(P)$ qua ${{N}_{2}}$ nên $c=2a-3b.$

Mặt phẳng $(P)$ cắt mặt cầu $(S)$ theo giao tuyến là đường tròn có bán kính bằng $r=\frac{\sqrt{210}}{6}$ nên ${{d}^{2}}(I;(P))={{R}^{2}}-{{r}^{2}}=14-\frac{210}{36}=\frac{49}{6}$ $\Rightarrow d(I;(P))=\frac{7}{\sqrt{6}}.$

Do đó $\frac{7}{\sqrt{6}}=\frac{\left| 6a-3b+(2a-3b).(-2) \right|}{\sqrt{{{a}^{2}}+{{b}^{2}}+{{(2a-3b)}^{2}}}}.$

$\Leftrightarrow \sqrt 6 \left| {2a + 3b} \right| = 7\sqrt {5{a^2} – 12ab + 10{b^2}}$ $\Leftrightarrow 221{a^2} – 660ab + 435{b^2} = 0$ $\Leftrightarrow a = 2b$, $a = \frac{{218}}{{221}}b.$

Nếu $a=2b$ thì chọn $b=1$ ta có $a=2$, $c=1$ nên phương trình mặt phẳng $(P):2x+y+z+2=0.$

Nếu $a=\frac{218}{221}b$ thì chọn $b=221$ ta có $a=218$, $c=-227$ nên phương trình mặt phẳng $(P):218x+221y-227z-6=0.$

Vậy có hai mặt phẳng thỏa mãn là: $(P):2x+y+z+2=0$ và $(P):218x+221y-227z-6=0.$

<!-- chunk:7 level:4 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## Bài tập 1. Lập phương trình mặt cầu biết:

1. Mặt cầu có tâm $I(1;2;3)$ bán kính $R=\sqrt{5}.$

2. Mặt cầu $(S)$ có tâm nằm trên $Ox$ và đi qua $A(1;2;1)$, $B(3;1;-2).$

3. Mặt cầu $(S)$ có tâm $I(3;-2;4)$ và tiếp xúc với mặt phẳng $(P):2x-y+2z+4=0.$

4. Mặt cầu $(S)$ đi qua $C(2;-4;3)$ và các hình chiếu của $C$ lên ba trục tọa độ.

5. Mặt cầu $(S)$ có tâm nằm trên mặt phẳng $(Oxy)$ và đi qua $M(1;0;2)$, $N(-2;1;1)$ và $P(-1;-1;1).$

6. Có tâm $I(6;3;-4)$ và tiếp xúc với $Oy.$

<!-- chunk:8 level:4 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## Bài tập 2. Lập phương trình mặt cầu $(S)$, biết $(S)$:

1. Có tâm $I(1;1;2)$ và tiếp xúc với mặt phẳng $(P):x+2y+2z+1=0.$

2. Có bán kính $R=3$ và tiếp xúc với mặt phẳng $(P):x+2y+2z+3=0$ tại điểm $A(1;1;-3).$

3. Có tâm nằm trên đường thẳng $d:\frac{x-2}{-3}=\frac{y-1}{2}=\frac{z-1}{2}$ và tiếp xúc với hai mặt phẳng $(P):x+2y-2z-2=0$ và $(Q):x+2y-2z+4=0.$

4. Đi qua bốn điểm $A(0;1;0)$, $B(2;3;1)$, $C(-2;2;2)$ và $D(1;-1;2).$

5. Có tâm thuộc mặt phẳng $(P):x+y+z-2=0$ và đi qua ba điểm $A(2;0;1)$, $B(1;0;0)$, $C(1;1;1).$

6. Có tâm nằm trên đường thẳng 
$$
d:\left\{ \begin{align}
& x=-2 \\
& y=0 \\
\end{align} \right.
$$
 và tiếp xúc với hai mặt phẳng

$\left( P \right):x-2z-8=0$ và $\left( Q \right):2x-z+5=0.$

<!-- chunk:9 level:4 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## Bài tập 3. Trong không gian với hệ tọa độ $Oxyz$, cho bốn điểm $A\left( 3;3;0 \right)$, $B\left( 3;0;3 \right)$, $C\left( 0;3;3 \right)$, $D\left( 3;3;3 \right).$

1. Viết phương trình mặt cầu đi qua bốn điểm $A$, $B$, $C$, $D.$

2. Tìm tọa độ tâm đường tròn ngoại tiếp tam giác $ABC.$

<!-- chunk:10 level:4 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## Bài tập 4. Lập phương trình mặt cầu $S(I;R)$ biết:

1. Mặt cầu có tâm $I(2;3;1)$ và tiếp xúc với đường thẳng $\Delta :\frac{x+2}{1}=\frac{y-1}{2}=\frac{z+1}{-2}.$

2. Mặt cầu có tâm $I(1;3;5)$ và cắt ${\Delta}’:\frac{x-2}{-1}=\frac{y+3}{1}=\frac{z}{1}$ tại hai điểm $A$, $B$ sao cho $AB=12.$

3. Mặt cầu có tâm thuộc đường thẳng $d:\frac{x-2}{1}=\frac{y-3}{1}=\frac{z+1}{2}$, đi qua $M(2;3;20)$ và tiếp xúc với ${d}’:\frac{x+4}{3}=\frac{y+6}{2}=\frac{z+19}{-2}.$

<!-- chunk:11 level:4 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## Bài tập 5. Lập phương trình mặt cầu $S(I,R)$ biết:

1. Mặt cầu có tâm thuộc đường thẳng $\Delta :\frac{x+2}{1}=\frac{y-1}{2}=\frac{z+1}{-2}$ và tiếp xúc với mặt phẳng $({{\alpha }_{1}}):3x+2y+z-6=0$ và mặt phẳng $({{\alpha }_{2}}):2x+3y+z=0.$

2. Mặt cầu có tâm $I(1;3;5)$ và cắt ${\Delta}’:\frac{x-2}{-1}=\frac{y+3}{1}=\frac{z}{1}$ tại hai điểm $A$, $B$ sao cho $AB=12.$

3. Mặt cầu có tâm thuộc đường thẳng $d:\frac{x-2}{1}=\frac{y}{-1}=\frac{z-3}{2}$, đi qua $M(1;1;4)$ và tiếp xúc với ${d}’:\frac{x+2}{1}=\frac{y+2}{1}=\frac{z-4}{-4}.$

<!-- chunk:12 level:4 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## Bài tập 7. Cho mặt cầu $(S):{{(x-1)}^{2}}+{{y}^{2}}+{{(z-2)}^{2}}=9.$ Chứng minh rằng:

1. Mặt cầu tiếp xúc với mặt phẳng $(P):2x+2y+z+5=0.$ Tìm tọa độ tiếp điểm $M.$

2. Mặt cầu cắt đường thẳng $\Delta :\frac{x+3}{2}=\frac{y-1}{1}=\frac{z}{1}$ tại hai điểm phân biệt. Tìm tọa độ các giao điểm đó.

<!-- chunk:13 level:4 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## Bài tập 8. Lập phương trình mặt cầu $S(I;R)$ tiếp xúc với hai mặt phẳng: $({{\alpha }_{1}}):6x-3y-2z-35=0$, $({{\alpha }_{1}}):6x-3y-2z+63=0.$ Đồng thời mặt cầu:

1. Có một tiếp điểm là $A(5;-1;-1).$

2. Qua hai điểm $B(1;3;-2)$, $C(-1;0;-3).$

<!-- chunk:14 level:4 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## Bài tập 9. Lập phương trình đường thẳng $\Delta$ biết:

1. $\Delta$ song song với $(P):x-y+z=0$ và cắt đường thẳng ${{\Delta }_{1}}$, ${{\Delta }_{2}}$ lần lượt tại $A$, $B$ sao cho $AB=\sqrt{2}$ với${{\Delta }_{1}}:\frac{x}{1}=\frac{y}{1}=\frac{z}{2}$, ${{\Delta }_{2}}:\frac{x+1}{-2}=\frac{y}{1}=\frac{z-1}{1}.$

2. $\Delta$ thuộc mặt phẳng $(Q):x+y+z+2=0$, vuông góc với đường thẳng $d:\frac{x-3}{2}=\frac{y+2}{1}=\frac{z+1}{-1}$ đồng thời khoảng cách từ giao điểm của $d$ và $(Q)$ đến $\Delta$ bằng $\sqrt{42}.$

3. $\Delta$ qua điểm $C(0;5;0)$, vuông góc với đường thẳng ${{d}_{1}}$ và tiếp xúc với mặt cầu $(S)$ với ${{d}_{1}}:\frac{x+1}{1}=\frac{y-1}{-2}=\frac{z}{2}$ và

$(S):{{x}^{2}}+{{y}^{2}}+{{z}^{2}}-4x-6y-2z+5=0.$

<!-- chunk:15 level:4 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## Bài tập 10. Cho mặt cầu $(S):{{x}^{2}}+{{y}^{2}}+{{z}^{2}}+2x-4y+6z+m=0.$ Tìm $m$ sao cho:

1. Mặt cầu tiếp xúc với mặt phẳng $(P):x-2y+2z-1=0.$

2. Mặt cầu cắt mặt phẳng $(Q):2x-y-2z+1=0$ theo giao tuyến là một đường tròn có diện tích bằng $4\pi .$

3. Mặt cầu cắt đường thẳng $\Delta :\frac{x+1}{-1}=\frac{y}{2}=\frac{z-2}{-2}$ tại hai điểm phân biệt $A$, $B$ sao cho tam giác $IAB$ vuông ($I$ là tâm mặt cầu).

<!-- chunk:16 level:4 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## Bài tập 11. Trong không gian với hệ trục tọa độ $Oxyz:$

1. Cho đường thẳng $d$ là giao tuyến của hai mặt phẳng $(\alpha ):2x-2y-z+1=0$, $(\beta ):x+2y-2z-4=0$ và mặt cầu $(S)$ có phương trình ${{x}^{2}}+{{y}^{2}}+{{z}^{2}}+4x-6y+m=0.$ Tìm $m$ để đường thẳng $d$ cắt mặt cầu $(S)$ tại hai điểm phân biệt $A$, $B$ sao cho $AB=8.$

2. Cho mặt phẳng $\left( P \right):2x+2y+z-{{m}^{2}}-3m=0$ và mặt cầu $\left( S \right):{{\left( x-1 \right)}^{2}}+{{\left( y+1 \right)}^{2}}+{{\left( z-1 \right)}^{2}}=9.$ Tìm $m$ để mặt phẳng $(P)$ tiếp xúc với mặt cầu $(S)$. Với $m$ vừa tìm được hãy xác định tọa độ tiếp điểm.

3. Cho hai đường thẳng có phương trình:

${{\Delta }_{1}}:\frac{x+2}{2}=\frac{y+3}{5}=\frac{z-4}{-1}$, 
$$
{{\Delta }_{2}}:\left\{ \begin{align}
& x=3-t \\
& y=1 \\
& z=10+t \\
\end{align} \right.
$$
 $(t\in \mathbb{R}).$

Gọi $A$, $B$ lần lượt là các điểm trên ${{\Delta }_{1}}$, ${{\Delta }_{2}}$ sao cho $AB$ vuông góc với ${{\Delta }_{1}}$ và ${{\Delta }_{2}}.$ Lập phương trình mặt cầu tiếp xúc với ${{\Delta }_{1}}$ tại điểm $A$, tiếp xúc với ${{\Delta }_{2}}$ tại điểm $B.$

<!-- chunk:17 level:4 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## Bài tập 12. Cho đường tròn $(C)$ là giao tuyến của $(\alpha ):x-2y+2z+1=0$ và mặt cầu $(S):{{x}^{2}}+{{y}^{2}}+{{z}^{2}}-4x+6y+6z+17=0.$

1. Xác định tâm và bán kính của đường tròn $(C).$

2. Viết phương trình mặt cầu $(S’)$ chứa đường tròn $(C)$ và có tâm nằm trên $(P):x+y+z+3=0$.

<!-- chunk:18 level:4 source:https://toanmath.com/2019/03/mat-cau-trong-khong-gian.html -->
## Bài tập 13. Trong không gian với hệ toạ độ Đề-các vuông góc $Oxyz$ cho hai mặt phẳng song song có các phương trình tương ứng là: $({{P}_{1}}):2x-y+2z-1=0$, $({{P}_{2}}):2x-y+2z+5=0$ và điểm $A(-1;1;1)$ nằm trong khoảng giữa hai mặt phẳng đó. Gọi $(S)$ là mặt cầu bất kỳ qua $A$ và tiếp xúc với cả hai mặt phẳng $({{P}_{1}})$, $({{P}_{2}}).$

1. Chứng tỏ rằng bán kính của hình cầu $(S)$ là một hằng số và tính bán kính đó.

2. Gọi $I$ là tâm của hình cầu $(S)$ . Chứng tỏ rằng $I$ thuộc một đường tròn cố định. Xác định toạ độ của tâm và tính bán kính của đường tròn đó.