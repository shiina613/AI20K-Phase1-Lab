# Mệnh đề và tính đúng sai của mệnh đề

<!-- chunk:0 level:0 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
Bài viết hướng dẫn phương pháp giải một số bài toán xác định mệnh đề và xét tính đúng hoặc sai của một mệnh đề trong chương trình Đại số 10.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## **I. PHƯƠNG PHÁP GIẢI TOÁN

**+ Khẳng định đúng là mệnh đề đúng, khẳng định sai là mệnh đề sai.

+ Câu không phải là câu khẳng định hoặc câu khẳng định mà không có tính đúng – sai đều không phải là mệnh đề.

+ Tính đúng – sai có thể chưa xác định hoặc không biết nhưng chắc chắn hoặc đúng hoặc sai cũng là mệnh đề. Không có mệnh đề vừa đúng vừa sai hoặc không đúng cũng không sai.

Mệnh đề đúng, mệnh đề sai:

$\bar P$ đúng $\Leftrightarrow P$ sai, $\bar P$ sai $\Leftrightarrow P$ đúng.

$(P \Rightarrow Q)$ chỉ sai khi $P$ đúng và $Q$ sai.

Đặc biệt:

+ Nếu $P$ sai thì $(P \Rightarrow Q)$ luôn đúng dù $Q$ đúng hoặc sai.

+ Nếu $Q$ đúng thì $(P \Rightarrow Q)$ luôn đúng dù $P$ đúng hoặc sai.

$(P \Leftrightarrow Q)$ chỉ đúng khi $P$ và $Q$ cùng đúng hoặc cùng sai.

Mệnh đề chứa dấu $\forall$, $\exists$:
$\forall x \in X$, $P(x)$ đúng $\Leftrightarrow$ với mọi ${x_0} \in X$, $P\left( {{x_0}} \right)$ đúng.

$\forall x \in X$, $P(x)$ sai $\Leftrightarrow$ có ${x_0} \in X$, $P\left( {{x_0}} \right)$ sai.

$\exists x \in X$, $P(x)$ đúng $\Leftrightarrow$ có ${x_0} \in X$, $P\left( {{x_0}} \right)$ đúng.

$\exists x \in X$, $P(x)$ sai $\Leftrightarrow$ mọi ${x_0} \in X$, $P\left( {{x_0}} \right)$ sai.

<!-- chunk:2 level:4 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## Bài tập 1: Xét xem các phát biểu sau có phải là mệnh đề không? Nếu là mệnh đề thì cho biết đó là mệnh đề đúng hay sai?

a) $A:$ $\sqrt 2$ là một số nguyên dương.

b) $B:$ Brazil là một nước thuộc Châu Âu phải không?

c) $C:$ Phương trình ${x^4} + 5x – 6 = 0$ vô nghiệm.

d) $D:$ Chứng minh bằng phản chứng khó thật!

e) $E:$ $– 5{\rm{ }}x – 6$ là một số âm.

f) $F:$ Nếu $n$ là số chẵn thì $n$ chia hết cho $4.$

g) $G:$ Nếu $n$ chia hết cho $4$ thì $n$ là số chẵn.

h) $H:$ $n$ là số chẵn nếu và chỉ nếu ${n^2}$ chia hết cho $4.$

i) $I:$ $\exists n \in N$, ${n^8} – n$ không là bội của $3.$

k) $K:$ $\forall x \in R$, ${x^2} – x + 1 > 0.$

a) $A$ là một mệnh đề sai.

b) $B$ là một câu hỏi, không phải là một mệnh đề.

c) $C$ là mệnh đề sai vì phương trình trên có ít nhất một nghiệm là $x = 1.$

d) $D$ là một câu cảm thán, không phải là mệnh đề.

e) $E$ không phải là mệnh đề. Đây là mệnh đề chứa biến.

f) $F$ là mệnh đề sai vì $n$ là số chẵn nhưng nó chưa chắc chia hết cho $4.$

g) $G$ là mệnh đề đúng.

h) $H$ là mệnh đề đúng.

i) $I$ là mệnh đề sai vì $\forall n \in N$, ${n^8} – n$ $= (n – 1)n(n + 1) \vdots 3.$

k) $K$ là mệnh đề đúng vì $\forall x \in R$, ${x^2} – x + 1$ $= {\left( {x – \frac{1}{2}} \right)^2} + \frac{3}{4} > 0.$

<!-- chunk:3 level:4 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## Bài tập 2: Các mệnh đề sau đúng hay sai, vì sao?

a) $\exists x \in N$, $3{x^2} – 5x + 2 = 0.$

b) $\forall x \in R$, $(x – 4)(x + 2) < 0.$

c) Nếu $\Delta ABC$ có $G$ là trọng tâm thì $\overrightarrow {GB} + \overrightarrow {GC} = – \overrightarrow {GA} .$

d) Một tứ giác là hình thoi khi và chỉ khi nó có hai đường chéo vuông góc với nhau tại trung điểm mỗi đường.

a) $\exists x \in N$, $3{x^2} – 5x + 2 = 0$ đúng vì $x = 1$ thỏa $3{x^2} – 5x + 2 = 0.$

b) $\forall x \in R$, $(x – 4)(x + 2) < 0$ sai vì $x = 5$ không thỏa $(x – 4)(x + 2) < 0.$

c) Mệnh đề “Nếu $\Delta ABC$ có $G$ là trọng tâm thì $\overrightarrow {GB} + \overrightarrow {GC} = – \overrightarrow {GA}$” đúng vì tính chất trọng tâm cho ta $\overrightarrow {GA} + \overrightarrow {GB} + \overrightarrow {GC} = \vec 0.$

d) Là mệnh đề đúng.

<!-- chunk:4 level:4 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## Bài tập 3: Xét tính đúng, sai của các mệnh đề sau và chứng minh điều đó:

$A:$ “Hai tam giác bằng nhau khi và chỉ khi chúng có diện tích bằng nhau”.

$B:$ “$\exists n \in N$, $(n + 3)(n + 4)$ là số nguyên tố”.

$C:$ “Trong $\Delta ABC$, nếu góc $\widehat A$ nhọn thì $AI > BI$ (với $I$ là trung điểm của $BC$)”.

$A$ sai vì chẳng hạn hai tam giác vuông có hai cạnh góc vuông là $1$, $4$ và $2$, $2$ đều có diện tích bằng $2$ nhưng không bằng nhau.

$B$ sai vì $x = (n + 3)(n + 4)$ nên $x$ có $2$ ước là $n + 3$ và $n + 4$ đều lớn hơn $1$ (do $n \in N$), suy ra $x$ là hợp số.

Giả sử $AI \le BI = CI$ 
$$
\Rightarrow \left\{ {\begin{array}{l}
{\widehat B \le \widehat {{A_1}}}\\
{\widehat C \le \widehat {{A_2}}}
\end{array}} \right.
$$
 $\Rightarrow \widehat B + \widehat C \le \widehat {{A_1}} + \widehat {{A_2}}$ $\Rightarrow \widehat B + \widehat C \le \widehat {BAC}.$

$\Rightarrow \widehat B + \widehat C + \widehat {BAC} \le 2\widehat {BAC}$ $\Rightarrow {90^0} \le \widehat A$ (mâu thuẫn).

Vậy $C$ đúng.

<img link="data_for_rag/toan10/images/menh-de-va-tinh-dung-sai-cua-menh-de-1.png" alt="">

<!-- chunk:5 level:4 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## Bài tập 4: Xét tính đúng, sai của mệnh đề sau:

a) Nếu $3 < 5$ thì $3 < 7.$

b) Nếu $45$ tận cùng bằng $5$ thì $45$ chia hết cho $25.$

c) Nếu $\sqrt 2$ không phải là một số vô tỉ thì $2\sqrt 2$ không là một số vô tỉ.

d) ${( – 5)^2} = {5^2}$ $\Leftrightarrow – 5 = 5.$

e) Tứ giác $ABCD$ là hình bình hành $\Leftrightarrow$ Tứ giác $ABCD$ có các góc đối bằng nhau.

a) Đặt $P =$ “$3 < 5$” và $Q=$ “$3 < 7$”.

Ta có mệnh đề đã cho có dạng “$P \Rightarrow Q$”. Ta thấy $P$ đúng và $Q$ đúng, do đó mệnh đề đã cho đúng.

b) Đặt $P =$ “$45$ tận cùng bằng $5$” và $Q=$ “$45$ chia hết cho $25$”. Ta có mệnh đề đã cho có dạng “$P \Rightarrow Q$”. Ta thấy $P$ đúng $Q$ sai, do đó mệnh đề đã cho sai.

c) Đặt $P=$ “$\sqrt 2$ không là số vô tỉ” và $Q =$ “$2\sqrt 2$ không là số vô tỉ”. Ta có mệnh đề đã cho có dạng”$P \Rightarrow Q$”. Ta thấy $P$ sai và $Q$ sai, do đó mệnh đề đã cho đúng.

d) Đặt $P =$ “${( – 5)^2} = {5^2}$” và $Q =$ “$-5 = 5$”. Ta có mệnh đề đã cho có dạng “$P \Leftrightarrow Q$”. Ta thấy $P$ đúng và $Q$ sai, do đó mệnh đề đã cho sai.

e) Đặt $P =$ “Tứ giác $ABCD$ là hình bình hành” và $Q=$ “Tứ giác $ABCD$ có các góc đối bằng nhau”. Ta có mệnh đề đã cho có dạng”$P \Leftrightarrow Q$”. Ta thấy $P$ và $Q$ cùng đúng hoặc cùng sai, do đó mệnh đề đã cho đúng.

<!-- chunk:6 level:4 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## Bài tập 5: Cho tam giác $ABC.$ Xét hai mệnh đề $P:$ “Tam giác $ABC$ vuông” và $Q:$ “$A{B^2} + A{C^2} = B{C^2}$”. Phát biểu và cho biết mệnh đề sau đúng hay sai?

a) $P \Rightarrow Q.$

b) $Q \Rightarrow P.$

a) Mệnh đề $P \Rightarrow Q$ là “Nếu tam giác $ABC$ vuông thì $A{B^2} + A{C^2} = B{C^2}$”.

Mệnh đề $P \Rightarrow Q$ sai vì chưa chắc tam giác đã cho vuông tại $A.$

b) Mệnh đề $Q \Rightarrow P$ là “Nếu ta có $A{B^2} + A{C^2} = B{C^2}$ thì $ABC$ là tam giác vuông”.

Mệnh đề $A{B^2} + A{C^2} = B{C^2}$ đúng (theo định lí Pitago).

<!-- chunk:7 level:4 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## Bài tập 6: Cho tam giác $ABC.$ Lập mệnh đề $P \Rightarrow Q$ và mệnh đề đảo của nó, rồi xét tính đúng sai của chúng khi:

a) $P:$ “Góc $A$ bằng ${90^0}$” và $Q:$ “Cạnh $BC$ lớn nhất”.

b) $P:$ “$\widehat A = \widehat B$” và $Q:$ “Tam giác $ABC$ cân”.

a) Mệnh đề $P \Rightarrow Q$ là “Nếu góc $A$ bằng ${90^0}$ thì cạnh $BC$ lớn nhất”. Đây là mệnh đề đúng.

Mệnh đề $Q \Rightarrow P$ là “Nếu cạnh $BC$ lớn nhất thì góc $A$ bằng ${90^0}$”. Đây là mệnh đề sai.

b) Mệnh đề $P \Rightarrow Q$ là “Nếu $\widehat A = \widehat B$ thì tam giác $ABC$ cân”. Đây là mệnh đề đúng.

Mệnh đề $Q \Rightarrow P$ là “Nếu tam giác $ABC$ cân thì $\widehat A = \widehat B$”. Đây là mệnh đề sai vì tam giác $ABC$ chưa chắc cân tại $C.$

<!-- chunk:8 level:4 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## Bài tập 7: Phát biểu mệnh đề $P \Rightarrow Q$ và phát biểu mệnh đề đảo, xét tính đúng sai của nó.

a) $P:$ “Tứ giác $ABCD$ là hình chữ nhật” và $Q:$ “Tứ giác $ABCD$ có hai đường thẳng $AC$ và $BD$ vuông góc nhau”.

b) $P:$ “$– \sqrt 3 > – \sqrt 2$” và $Q:$ “${\left( { – \sqrt 3 } \right)^5} > {\left( { – \sqrt 2 } \right)^5}$”.

c) $P:$ “Tam giác $ABC$ có $\widehat A = \widehat B + \widehat C$” và $Q:$ “Tam giác $ABC$ có $B{C^2} = A{B^2} + A{C^2}$”.

d) $P:$ “Tố Hữu là nhà toán học lớn của Việt Nam” và $Q:$ “Évariste Galois là nhà thơ lỗi lạc của thế giới”.

a) Mệnh đề $P \Rightarrow Q$ là “Nếu tứ giác $ABCD$ là hình chữ nhật thì tứ giác $ABCD$ có hai đường thẳng $AC$ và $BD$ vuông góc với nhau”. Đây là mệnh đề sai.

Mệnh đề đảo $Q \Rightarrow P$ là “Nếu tứ giác $ABCD$ có hai đường thẳng $AC$ và $BD$ vuông góc với nhau thì tứ giác $ABCD$ là hình chữ nhật”. Đây là mệnh đề sai.

b) Mệnh đề $P \Rightarrow Q$ là “Nếu $– \sqrt 3 > – \sqrt 2$ thì ${\left( { – \sqrt 3 } \right)^5} > {\left( { – \sqrt 2 } \right)^5}$”. Đây là mệnh đề đúng.

Mệnh đề đảo $Q \Rightarrow P$ là “Nếu ${\left( { – \sqrt 3 } \right)^5} > {\left( { – \sqrt 2 } \right)^5}$ thì $– \sqrt 3 > – \sqrt 2$”. Đây là mệnh đề đúng.

c) Mệnh đề $P \Rightarrow Q$ là “Nếu tam giác $ABC$ có $\widehat A = \widehat B + \widehat C$ thì nó có $B{C^2} = A{B^2} + A{C^2}$”.Đây là mệnh đề đúng.

Mệnh đề đảo $Q \Rightarrow P$ là “Nếu tam giác $ABC$ có $B{C^2} = A{B^2} + A{C^2}$ thì $\widehat A = \widehat B + \widehat C$”. Đây là mệnh đề đúng.

d) Mệnh đề $P \Rightarrow Q$ là “Nếu Tố Hữu là toán học lớn của Việt Nam thì Évariste Galois là nhà thơ lỗi lạc của thế giới”. Đây là mệnh đề đúng.

Mệnh đề đảo $Q \Rightarrow P$ là “Nếu Évariste Galois là nhà thơ lỗi lạc của thế giới thì Tố Hữu là nhà toán học lớn của Việt Nam”. Đây là mệnh đề đúng.

<!-- chunk:9 level:4 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## Bài tập 8: Cho mệnh đề $A:$ “Nếu $3n + 2$ là số nguyên lẻ thì $n$ là số nguyên lẻ”. Hãy viết mệnh đề đảo của $A$ và giải thích tính đúng, sai của mệnh đề đảo ấy.

$A:$ “Nếu $3n + 2$ là số nguyên lẻ thì $n$ là số nguyên lẻ”.

Mệnh đề đảo của $A$ là mệnh đề $B:$ “Nếu $n$ là số nguyên lẻ thì $3n + 2$ là số nguyên lẻ”.

Giải thích: Giả sử $n = 2k + 1$ $(k \in Z)$ $\Rightarrow 3n + 2 = 6k + 5$ $\Rightarrow 3n + 2 = 2(3k + 2) + 1.$

$\Rightarrow 3n + 2 = 2k’ + 1$ $\left( {k’ = 3k + 2 \in Z} \right).$

Vậy $3n + 2$ là số nguyên lẻ nên $B$ đúng.

<!-- chunk:10 level:4 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## Bài tập 9: Phát biểu mệnh đề $P \Rightarrow Q$ và phát biểu mệnh đề đảo, xét tính đúng sai của nó.

a) $P:$ “Tứ giác $ABCD$ là hình thoi” và $Q:$ “Tứ giác $ABCD$ có $AC$ và $BD$ cắt nhau tại trung điểm của mỗi đường”.

b) $P:$ “$2 > 9$” và $Q:$ “$4 < 3$”.

c) $P:$ “Tam giác $ABC$ vuông cân tại $A$” và $Q:$ “Tam giác $ABC$ có $\widehat A = 2\widehat B$”.

a) Mệnh đề $P \Rightarrow Q$ là “Nếu tứ giác $ABCD$ là hình thoi thì $AC$ và $BD$ cắt nhau tại trung điểm mỗi đường”. Đây là mệnh đề đúng.

Mệnh đề đảo $Q \Rightarrow P$ là “Nếu tứ giác $ABCD$ có $AC$ và $BD$ cắt nhau tại trung điểm mỗi đường thì $ABCD$ là hình thoi”. Đây là mệnh đề sai.

b) Mệnh đề $P \Rightarrow Q$ là “Nếu $2 > 9$ thì $4 < 3$”. Đây là mệnh đề đúng.

Mệnh đề đảo $Q \Rightarrow P$ là “Nếu $4 < 3$ thì $2 > 9$”. Đây là mệnh đề đúng.

c) Mệnh đề $P \Rightarrow Q$ là “Nếu tam giác $ABC$ vuông cân tại $A$ thì $\widehat A = 2\widehat B$” Đây là mệnh đề đúng.

Mệnh đề đảo $Q \Rightarrow P$ là “Nếu tam giác $ABC$ có $\widehat A = 2\widehat B$ thì nó vuông cân tại $A$”. Đây là mệnh đề sai.

<!-- chunk:11 level:4 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## Bài tập 10: Phát biểu mệnh đề $P \Leftrightarrow Q$ bằng hai cách và xét tính đúng sai của nó:

$P:$ “Tứ giác $ABCD$ là hình thoi” và $Q:$ “Tứ giác $ABCD$ là hình bình hành có hai đường chéo vuông góc với nhau”.

Cách 1: “Tứ giác $ABCD$ là hình thoi khi và chỉ khi tứ giác $ABCD$ là hình bình hành có hai đường chéo vuông góc với nhau”.

Cách 2: “Tứ giác $ABCD$ là hình thoi nếu và chỉ nếu tứ giác $ABCD$ là hình bình hành có hai đường chéo vuông góc với nhau”.

Mệnh đề $P \Leftrightarrow Q$ đúng vì mệnh đề $P \Rightarrow Q$ đúng và mệnh đề $Q \Rightarrow P$ đúng.

<!-- chunk:12 level:4 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## Bài tập 11: Lập mệnh đề kéo theo và mệnh đề tương đương của hai mệnh đề sau đây và cho biết tính đúng, sai của chúng:

$P:$ “Điểm $M$ nằm trên phân giác của góc $Oxy$” và $Q:$ “Điểm $M$ cách đều hai tia $Ox$, $Oy$”.

Mệnh đề $P \Rightarrow Q$ là “Nếu điểm $M$ nằm trên phân giác của góc $Oxy$ thì $M$ cách đều hai tia $Ox$, $Oy$”. Đây là mệnh đề đúng.

Mệnh đề $Q \Rightarrow P$ là “Nếu điểm $M$ cách đều hai tia $Ox$, $Oy$ thì $M$ nằm trên phân giác của góc $Oxy$”. Đây là mệnh đề đúng.

Mệnh đề $P \Leftrightarrow Q$ là “Điểm $M$ nằm trên phân giác của góc $Oxy$ nếu và chỉ nếu (khi và chỉ khi) điểm $M$ cách đều hai tia $Ox$, $Oy$”. Đây là mệnh đề đúng.

<!-- chunk:13 level:4 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## Bài tập 12: Phát biểu mệnh đề $P \Leftrightarrow Q$ bằng hai cách và xét tính đúng sai của nó.

a) Cho tứ giác $ABCD.$ Xét hai mệnh đề:

$P:$ “Tứ giác $ABCD$ là hình vuông”.

$Q:$ “Tứ giác $ABCD$ là hình chữ nhật có hai đường chéo bằng và vuông góc với nhau”.

b) $P:$ “Bất phương trình ${x^2} – 3x + 1 > 0$ có nghiệm” và $Q:$ “Bất phương trình ${x^2} – 3x + 1 \le 0$ vô nghiệm”.

a) Ta có mệnh đề $P \Leftrightarrow Q$ đúng vì mệnh đề $P \Rightarrow Q$, $Q \Rightarrow P$ đều đúng và được phát biểu bằng hai cách như sau:

Cách 1: “Tứ giác $ABCD$ là hình vuông khi và chỉ khi tứ giác $ABCD$ là hình chữ nhật có hai đường chéo bằng và vuông góc với nhau”.

Cách 2: “Tứ giác $ABCD$ là hình vuông nếu và chỉ nếu tứ giác $ABCD$ là hình chữ nhật có hai đường chéo bằng và vuông góc với nhau”.

b) Ta có mệnh đề $P \Leftrightarrow Q$ sai vì mệnh đề $P$ đúng còn $Q$ sai. Phát biểu mệnh đề $P \Leftrightarrow Q$ bằng hai cách như sau:

Cách 1: “Bất phương trình ${x^2} – 3x + 1 > 0$ có nghiệm khi và chỉ khi bất phương trình ${x^2} – 3x + 1 \le 0$ vô nghiệm”.

Cách 2: “Bất phương trình ${x^2} – 3x + 1 > 0$ có nghiệm nếu và chỉ nếu bất phương trình ${x^2} – 3x + 1 \le 0$ vô nghiệm”.

<!-- chunk:14 level:4 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## Bài tập 13: Cho tam giác $ABC$ có đường trung tuyến $AM.$ Xét hai mệnh đề sau:

$P:$ “Tam giác $ABC$ vuông tại $A$”.

$Q:$ “Trung tuyến $AM$ bằng nửa cạnh $BC$”.

a) Phát biểu mệnh đề $P \Rightarrow Q$ và cho biết mệnh đề này đúng hay sai.

b) Phát biểu mệnh đề $P \Leftrightarrow Q$ và cho biết mệnh đề này đúng hay sai.

a) $(P \Rightarrow Q)$: “Nếu tam giác $ABC$ vuông tại $A$ thì độ dài trung tuyến $AM$ bằng một nửa cạnh $BC$”.

Ta thấy nếu $P$ đúng thì tam giác $ABC$ vuông tại $A.$ Khi đó $AM = \frac{1}{2}BC$ nên $Q$ đúng. Do đó $(P \Rightarrow Q)$ là mệnh đề đúng.

b) $(P \Leftrightarrow Q)$: “Tam giác $ABC$ vuông tại $A$ khi và chỉ khi độ dài trung tuyến $AM$ bằng một nửa cạnh $BC$”.

Ta thấy nếu $P$ đúng thì $Q$ cũng đúng và nếu $P$ sai thì $Q$ cũng sai. Do đó $P$ và $Q$ cùng đúng hoặc cùng sai. Do đó $(P \Leftrightarrow Q)$ là mệnh đề đúng.

<!-- chunk:15 level:4 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## Bài tập 14: Xét hai mệnh đề sau:

$P:$ “$120$ chia hết cho $6$ và chia hết cho $8$”.

$Q:$ “$120$ chia hết cho $6.8$”.

a) Phát biểu mệnh đề $P \Rightarrow Q$ và cho biết mệnh đề này đúng hay sai.

b) Phát biểu mệnh đề $P \Leftrightarrow Q$ và cho biết mệnh đề này đúng hay sai.

a) $(P \Rightarrow Q)$: “Nếu $120$ chia hết cho $6$ và chia hết cho $8$ thì $120$ chia hết cho $6.8$”.

Ta thấy: $P$ là mệnh đề đúng và $Q$ là mệnh đề sai. Vậy $(P \Rightarrow Q)$ sai.

b) $(P \Leftrightarrow Q)$: “$120$ chia hết cho $6$ và chia hết cho $8$ khi và chỉ khi $120$ chia hết cho $6.8$”.

Ta thấy: $P$ là mệnh đề đúng và $Q$ là mệnh đề sai. Vậy $(P \Leftrightarrow Q)$ sai.

<!-- chunk:16 level:1 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## III. BÀI TẬP TRẮC NGHIỆM TỰ LUYỆN
## Câu 1. Trong các mệnh đề sau, mệnh đề nào sai?

A. $– \pi < – 2 \Leftrightarrow {\pi ^2} < 4.$

B. $\pi < 4 \Leftrightarrow {\pi ^2} < 16.$

C. $\sqrt {23} < 5 \Rightarrow 2\sqrt {23} < 2.5.$

D. $\sqrt {23} < 5 \Rightarrow – 2\sqrt {23} > – 2.5.$

## Câu 2. Mệnh đề nào sau là mệnh đề sai?

A. $\forall n \in N:$ $n \le 2n.$

B. $\exists n \in N:$ ${n^2} = n.$

C. $\forall x \in R:$ ${x^2} > 0.$

D. $\exists x \in R:$ $x > {x^2}.$

## Câu 3. Trong các mệnh đề sau, tìm mệnh đề đúng?

A. $\forall x \in R:$ ${x^2} > 0.$

B. $\forall x \in N:$ $x \vdots 3.$

C. $\exists x \in R:$ ${x^2} < 0.$

D. $\exists x \in R:$ $x > {x^2}.$

## Câu 4. Trong các mệnh đề sau, mệnh đề nào đúng?

A. $\forall n \in N$, ${n^2} + 1$ không chia hết cho $3.$

B. $\forall x \in R$, $|x| < 3 \Leftrightarrow x < 3.$

C. $\forall x \in R$, ${(x – 1)^2} \ne x – 1.$

D. $\exists n \in N$, ${n^2} + 1$ chia hết cho $4.$

## Câu 5. Trong các mệnh đề sau, mệnh đề nào sai?

A. $\exists x \in Q$, $4{x^2} – 1 = 0.$

B. $\forall n \in N$, ${n^2} > n.$

C. $\exists x \in R$, $x > {x^2}.$

D. $\forall n \in N$, ${n^2} + 1$ không chia hết cho $3.$

## Câu 6. Chọn mệnh đề đúng trong các mệnh đề sau đây:

A. $\forall x \in R$, $x > 3 \Rightarrow {x^2} > 9.$

B. $\forall x \in R$, $x > – 3$ $\Rightarrow {x^2} > 9.$

C. $\forall x \in R$, ${x^2} > 9 \Rightarrow x > 3.$

D. $\forall x \in R$, ${x^2} > 9 \Rightarrow x > – 3.$

## Câu 7. Trong các mệnh đề sau, mệnh đề nào sai?

A. $\forall n \in N$, ${n^2} \vdots 2 \Rightarrow n \vdots 2.$

B. $\forall n \in N$, ${n^2} \vdots 6 \Rightarrow n \vdots 6.$

C. $\forall n \in N$, ${n^2} \vdots 3 \Rightarrow n \vdots 3.$

D. $\forall n \in N$, ${n^2} \vdots 9 \Rightarrow n \vdots 9.$

## Câu 8. Cho $x$ là số thực, mệnh đề nào sau đây đúng?

A. $\forall x$, ${x^2} > 5$ $\Rightarrow x > \sqrt 5$ hoặc $x < – \sqrt 5 .$

B. $\forall x$, ${x^2} > 5$ $\Rightarrow – \sqrt 5 < x < \sqrt 5 .$

C. $\forall x$, ${x^2} > 5$ $\Rightarrow x > \pm \sqrt 5 .$

D. $\forall x$, ${x^2} > 5$ $\Rightarrow x \ge \sqrt 5$ hoặc $x \le – \sqrt 5 .$

## Câu 9. Trong các mệnh đề sau đây, mệnh đề nào sai?

<!-- chunk:17 level:1 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## D. Một tam giác là đều khi và chỉ khi chúng có hai đường trung tuyến bằng nhau và có một góc bằng ${60^0}.$

## Câu 10. Trong các mệnh đề sau đây, mệnh đề nào có mệnh đề đảo là đúng?

<!-- chunk:18 level:1 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## D. Nếu một số tận cùng bằng $0$ thì số đó chia hết cho $5.$

## Câu 11. Trong các mệnh đề sau, mệnh đề nào có mệnh đề đảo là sai?

<!-- chunk:19 level:1 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## D. Nếu tứ giác có hai đường chéo vuông góc thì tứ giác đó là hình thoi.

## Câu 12. Trong các mệnh đề sau đây, mệnh đề nào sai?

A. $n$ là số lẻ khi và chỉ khi ${n^2}$ là số lẻ.

B. $n$ chia hết cho $3$ khi và chỉ khi tổng các chữ số của $n$ chia hết cho $3.$

<!-- chunk:20 level:1 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## D. Tam giác $ABC$ là tam giác đều khi và chỉ khi $AB = AC$ và có một góc bằng ${60^0}.$

## Câu 13. Phát biểu nào sau đây là mệnh đề đúng?

A. $2.5 = 10$ $\Rightarrow$ Luân Đôn là thủ đô của Hà Lan.

B. $7$ là số lẻ $\Rightarrow$ $7$ chia hết cho $2.$

C. $81$ là số chính phương $\Rightarrow \sqrt {81}$ là số nguyên.

<!-- chunk:21 level:1 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## D. Số $141$ chia hết cho $3$ $\Rightarrow$ $141$ chia hết cho $9.$

## Câu 14. Mệnh đề nào sau đây sai?

<!-- chunk:22 level:1 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## D. Hai tam giác vuông $ABC$ và $A’B’C’$ có diện tích bằng nhau $\Leftrightarrow \Delta ABC = \Delta A’B’C’.$

## Câu 16. Tìm mệnh đề sai.

A. $10$ chia hết cho $5$ $\Leftrightarrow$ Hình vuông có hai đường chéo bằng nhau và vuông góc nhau.

<!-- chunk:23 level:1 source:https://toanmath.com/2019/11/menh-de-va-tinh-dung-sai-cua-menh-de.html -->
## C. Hình thang $ABCD$ nội tiếp đường tròn $(O)$ $\Leftrightarrow ABCD$ là hình thang cân.

D. $63$ chia hết cho $7$ $\Rightarrow$ Hình bình hành có hai đường chéo vuông góc nhau.

## Câu 17. Cho tam giác $ABC$ cân tại $A$, $I$ là trung điểm $BC.$ Mệnh đề nào sau đây đúng?

A. $\exists M \in AI$, $MA = MC.$

B. $\forall M$, $MB = MC.$

C. $\forall M \in AB$, $MB = MC.$

D. $\exists M \notin AI$, $MB = MC.$

## Câu 18. Với giá trị thực nào của $x$ thì mệnh đề chứa biến $P(x):$ “${x^2} – 3x + 2 = 0$ là mệnh đề đúng?

A. $0.$

B. $1.$

C. $-1.$

D. $-2.$

## Câu 19. Với giá trị nào của $n$, mệnh đề chứa biến $P(n):$ “$n$ chia hết cho $12$” là đúng?

A. $48.$

B. $4.$

C. $3.$

D. $88.$

## Câu 20. Cho mệnh đề chứa biến $P(x):$ “với $x \in R$, $\sqrt x \ge x$”. Mệnh đề nào sau đây sai?

A. $P(0).$

B. $P(1).$

C. $P\left( {\frac{1}{2}} \right)$.

D. $P(2)$.

## Câu 21. Với giá trị nào của $x$, mệnh đề chứa biến $P(x):$ “${x^2} – 5x + 4 = 0$” là mệnh đề đúng?

A. $0.$

B. $5.$

C. $\frac{4}{5}.$

D. $1.$

## Câu 22. Cho mệnh đề chứa biến $P(x)$: “$x + 15 \le {x^2}$” với $x$ là số thực. Mệnh đề nào sau đây là đúng?

A. $P(0).$

B. $P(3).$

C. $P(4).$

D. $P(5).$

## Câu 23. Cho $n$ là số tự nhiên, mệnh đề nào sau đây đúng?

A. $\forall n$, $n(n + 1)$ là số chính phương.

B. $\forall n$, $n(n + 1)$ là số lẻ.

C. $\exists n$, $n(n + 1)(n + 2)$ là số lẻ.

D. $\forall n$, $n(n + 1)(n + 2)$ là số chia hết cho $6.$

## Câu 24. Chọn mệnh đề đúng:

A. $\forall x \in N$, ${n^2} – 1$ là bội số của $3.$

B. $\exists x \in Q$, ${x^2} = 3.$

C. $\forall x \in N$, ${2^n} + 1$ là số nguyên tố.

D. $\forall x \in N$, ${2^n} \ge n + 2.$

## Câu 25. Biết $A$ là mệnh đề sai, còn $B$ là mệnh đề đúng. Mệnh đề nào sau đây đúng?

A. ${B \Rightarrow A.}$

B. ${B \Leftrightarrow A}$.

C. ${\bar A \Leftrightarrow \bar B}$.

D. ${B \Rightarrow \bar A}$.

## Câu 26. Biết $A$ là mệnh đề đúng, $B$ là mệnh đề sai, $C$ là mệnh đề đúng. Mệnh đề nào sau đây sai?

A. $A \Rightarrow C$.

B. $C \Rightarrow (A \Rightarrow \bar B).$

C. $(\bar B \Rightarrow C) \Rightarrow A$.

D. $C \Rightarrow (A \Rightarrow B)$.

## Câu 27. Cho $A$, $B$, $C$ là ba mệnh đề đúng, mệnh đề nào sau đây là đúng?

A. $A \Rightarrow (B \Rightarrow \bar C)$.

B. $C \Rightarrow \bar A$.

C. $B \Rightarrow (\overline {A \Rightarrow C} )$.

D. $C \Rightarrow (A \Rightarrow B)$.

## Câu 28. Cho ba mệnh đề:

$P:$ “Số $20$ chia hết cho $5$ và chia hết cho $2$”.

$Q:$ “Số $35$ chia hết cho $9$”.

$R:$ “Số $17$ là số nguyên tố”.

Hãy tìm mệnh đề sai trong các mệnh đề dưới đây.

A. $P \Leftrightarrow (\bar Q \Rightarrow R).$

B. $R \Leftrightarrow \bar Q.$

C. $(R \Rightarrow P) \Rightarrow Q$.

D. $(\bar Q \Rightarrow R) \Rightarrow P$.