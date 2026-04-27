# Các dạng toán về mệnh đề và mệnh đề chứa biến

<!-- chunk:0 level:0 source:https://toanmath.com/2018/06/cac-dang-toan-ve-menh-de-va-menh-de-chua-bien.html -->
Bài viết tóm tắt lý thuyết và hướng dẫn giải các dạng toán về mệnh đề và mệnh đề chứa biến thông qua các ví dụ minh họa cụ thể.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/06/cac-dang-toan-ve-menh-de-va-menh-de-chua-bien.html -->
## A. TÓM TẮT LÝ THUYẾT

1. Định nghĩa mệnh đề

Mệnh đề là một câu khẳng định ĐÚNG hoặc SAI.

Một mệnh đề không thể vừa đúng hoặc vừa sai.

2. Mệnh đề phủ định

Cho mệnh đề $P$, mệnh đề “không phải $P$” gọi là mệnh đề phủ định của $P$, ký hiệu là $\overline{P}$.

Nếu $P$ đúng thì $\overline{P}$ sai, nếu $P$ sai thì $\overline{P}$ đúng.

3. Mệnh đề kéo theo và mệnh đề đảo

Cho hai mệnh đề $P$ và $Q$, mệnh đề “nếu $P$ thì $Q$” gọi là mệnh đề kéo theo, ký hiệu là $P\Rightarrow Q$.

Mệnh đề $P\Rightarrow Q$ chỉ sai khi $P$ đúng $Q$ sai.

Cho mệnh đề $P\Rightarrow Q$, khi đó mệnh đề $Q\Rightarrow P$ gọi là mệnh đề đảo của $Q\Rightarrow P.$

4. Mệnh đề tương đương

Cho hai mệnh đề $P$ và $Q$, mệnh đề “$P$ nếu và chỉ nếu $Q$” gọi là mệnh đề tương đương, ký hiệu là $P\Leftrightarrow Q$.

Mệnh đề $P\Leftrightarrow Q$ đúng khi cả $P\Rightarrow Q$ và $Q\Rightarrow P$ cùng đúng.

Chú ý: “Tương đương” còn được gọi bằng các thuật ngữ khác như “điều kiện cần và đủ”, “khi và chỉ khi”, “nếu và chỉ nếu”.

5. Mệnh đề chứa biến

Mệnh đề chứa biến là một câu khẳng định chứa biến nhận giá trị trong một tập $X$ nào đó mà với mỗi giá trị của biến thuộc $X$ ta được một mệnh đề.

6. Các kí hiệu $\forall$, $\exists$ và mệnh đề phủ định của mệnh đề có chứa kí hiệu $\forall$,$\exists$

Kí hiệu $\forall$: đọc là với mọi, $\exists$: đọc là tồn tại.

Phủ định của mệnh đề “$\forall x\in X,P\left( x \right)$ ” là mệnh đề “$\exists x\in X,\overline{P(x)}$”.

Phủ định của mệnh đề “$\exists x\in X,P\left( x \right)$ ” là mệnh đề “$\forall x\in X,\overline{P(x)}$”.

<!-- chunk:2 level:3 source:https://toanmath.com/2018/06/cac-dang-toan-ve-menh-de-va-menh-de-chua-bien.html -->
## Ví dụ 1: Các câu sau đây, câu nào là mệnh đề, câu nào không phải là mệnh đề? Nếu là mệnh đề hãy cho biết mệnh đề đó đúng hay sai.

$(1)$ Ở đây đẹp quá!

$(2)$ Phương trình ${{x}^{2}}-3x+1=0$ vô nghiệm.

$(3)$ $16$ không là số nguyên tố.

$(4)$ Hai phương trình ${{x}^{2}}-4x+3=0$ và ${{x}^{2}}-\sqrt{x+3}+1=0$ có nghiệm chung.

$(5)$ Số $\pi$ có lớn hơn $3$ hay không?

$(6)$ Italia vô địch Worldcup 2006.

$(7)$ Hai tam giác bằng nhau khi và chỉ khi chúng có diện tích bằng nhau.

$(8)$ Một tứ giác là hình thoi khi và chỉ khi nó có hai đường chéo vuông góc với nhau.

Câu $(1)$ và $(5)$ không là mệnh đề (vì là câu cảm thán, câu hỏi).

Các câu $(3)$, $(4)$, $(6)$, $(8)$ là những mệnh đề đúng.

Câu $(2)$ và $(7)$ là những mệnh đề sai.

<!-- chunk:3 level:3 source:https://toanmath.com/2018/06/cac-dang-toan-ve-menh-de-va-menh-de-chua-bien.html -->
## Ví dụ 2: Cho ba mệnh đề sau, với $n$ là số tự nhiên:

$(1)$ $n+8$ là số chính phương.

$(2)$ Chữ số tận cùng của $n$ là $4.$

$(3)$ $n-1$ là số chính phương.

Biết rằng có hai mệnh đề đúng và một mệnh đề sai. Hãy xác định mệnh đề nào, đúng mệnh đề nào sai?

Ta có số chính phương có các chữ số tận cùng là $0,1,4,5,6,9$. Vì vậy:

+ Nhận thấy giữa mệnh đề $(1)$ và $(2)$ có mâu thuẫn. Bởi vì, giả sử $2$ mệnh đề này đồng thời là đúng thì $n+8$ có chữ số tận cùng là $2$ nên không thể là số chính phương. Vậy trong hai mệnh đề này phải có một mệnh đề là đúng và một mệnh đề là sai.

+ Tương tự, nhận thấy giữa mệnh đề $(2)$ và $(3)$ cũng có mâu thuẫn. Bởi vì, giả sử mệnh đề này đồng thời là đúng thì $n-1$ có chữ số tận cùng là $3$ nên không thể là số chính phương.

Vậy trong ba mệnh đề trên thì mệnh đề $(1)$ và $(3)$ là đúng, còn mệnh đề $(2)$ là sai.

<!-- chunk:4 level:3 source:https://toanmath.com/2018/06/cac-dang-toan-ve-menh-de-va-menh-de-chua-bien.html -->
## Ví dụ 3: Nêu mệnh đề phủ định của các mệnh đề sau, cho biết mệnh đề này đúng hay sai?

$P:$ “Hình thoi có hai đường chéo vuông góc với nhau”.

$Q:$ “$6$ là số nguyên tố”.

$R:$ “Tổng hai cạnh của một tam giác lớn hơn cạnh còn lại”.

$S:$ “$5>-3$”.

$K:$ “Phương trình ${{x}^{4}}-2{{x}^{2}}+2=0$ có nghiệm”.

$H:$ “${{\left( \sqrt{3}-\sqrt{12} \right)}^{2}}=3$”.

Ta có các mệnh đề phủ định là:

$\overline{P}:$ “Hai đường chéo của hình thoi không vuông góc với nhau”, mệnh đề này sai.

$\overline{Q}:$ “$6$ không phải là số nguyên tố”, mệnh đề này đúng.

$\overline{R}:$ “Tổng hai cạnh của một tam giác nhỏ hơn hoặc bằng cạnh còn lại”, mệnh đề này sai.

$\overline{S}:$ “$5\le -3$”, mệnh đề này sai.

$\overline{K}:$ “Phương trình ${{x}^{4}}-2{{x}^{2}}+2=0$ vô nghiệm”, mệnh đề này đúng.

$\overline{H}:$ “${{\left( \sqrt{3}-\sqrt{12} \right)}^{2}}\ne 3$”, mệnh đề này sai.

<!-- chunk:5 level:3 source:https://toanmath.com/2018/06/cac-dang-toan-ve-menh-de-va-menh-de-chua-bien.html -->
## Ví dụ 4: Phát biểu mệnh đề $P\Rightarrow Q$ và phát biểu mệnh đề đảo, xét tính đúng sai của nó.

a. $P:$ “Tứ giác $ABCD$ là hình thoi” và $Q:$ “Tứ giác $ABCD$ có $AC$ và $BD$ cắt nhau tại trung điểm mỗi đường”.

b. $P:$ “$2>9$” và $Q:$ “$4<3$”.

c. $P:$ “Tam giác $ABC$ vuông cân tại $A$” và $Q:$ “Tam giác $ABC$ có $\widehat{A}=2\widehat{B}$”.

a. Mệnh đề $P\Rightarrow Q$: “Nếu tứ giác $ABCD$ là hình thoi thì $AC$ và $BD$ cắt nhau tại trung điểm mỗi đường”, mệnh đề này đúng.

Mệnh đề đảo $Q\Rightarrow P$: “Nếu tứ giác $ABCD$ có $AC$ và $BD$ cắt nhau tại trung điểm mỗi đường thì$ABCD$ là hình thoi”, mệnh đề này sai.

b. Mệnh đề $P\Rightarrow Q$: “Nếu $2>9$ thì $4<3$”, mệnh đề này đúng.

Mệnh đề đảo $Q\Rightarrow P$: “Nếu $4<3$ thì $2>9$”, mệnh đề này đúng.

c. Mệnh đề $P\Rightarrow Q$: “Nếu tam giác $ABC$ vuông cân tại $A$ thì $\widehat{A}=2\widehat{B}$”, mệnh đề này đúng.

Mệnh đề đảo $Q\Rightarrow P$: “Nếu tam giác $ABC$ có $\widehat{A}=2\widehat{B}$ thì nó vuông cân tại $A$”, mệnh đề này sai.

<!-- chunk:6 level:3 source:https://toanmath.com/2018/06/cac-dang-toan-ve-menh-de-va-menh-de-chua-bien.html -->
## Ví dụ 5: Phát biểu mệnh đề $P\Leftrightarrow Q$ và và xét tính đúng sai của nó.

a. $P:$ “Tứ giác $ABCD$ là hình thoi” và $Q:$ “Tứ giác $ABCD$ là hình bình hành có hai đường chéo vuông góc với nhau”.

b. $P:$ “Bất phương trình $\sqrt{{{x}^{2}}-3x}>1$ có nghiệm” và $Q:$ “$\sqrt{{{\left( -1 \right)}^{2}}-3.\left( -1 \right)}>1$”.

a. Mệnh đề $P \Leftrightarrow Q$: “Tứ giác $ABCD$ là hình thoi khi và chỉ khi tứ giác $ABCD$ là hình bình hành có hai đường chéo vuông góc với nhau”, mệnh đề này đúng vì mệnh đề $P \Rightarrow Q$, $Q \Rightarrow P$ đều đúng.

b. Mệnh đề $P \Leftrightarrow Q$: “Bất phương trình $\sqrt{{{x}^{2}}-3x}>1$ có nghiệm khi và chỉ khi $\sqrt{{{\left( -1 \right)}^{2}}-3.\left( -1 \right)}>1$”, mệnh đề này đúng vì mệnh đề $P, Q$ đều đúng, do đó mệnh đề $P\Rightarrow Q$, $Q \Rightarrow P$ đều đúng.

<!-- chunk:7 level:3 source:https://toanmath.com/2018/06/cac-dang-toan-ve-menh-de-va-menh-de-chua-bien.html -->
## Ví dụ 6: Cho mệnh đề chứa biến “$P\left( x \right):x>{{x}^{3}}$”, xét tính đúng sai của các mệnh đề sau:

a. $P\left( 1 \right).$

b. $P\left( \frac{1}{3} \right).$

c. $\forall x\in N, P\left( x \right).$

d. $\exists x\in N, P\left( x \right).$

a. Ta có $P\left( 1 \right): 1>{{1}^{3}}$ đây là mệnh đề sai.

b. Ta có $P\left( \frac{1}{3} \right): \frac{1}{3}>{{\left( \frac{1}{3} \right)}^{3}}$ đây là mệnh đề đúng.

c. Ta có $\forall x\in N, x>{{x}^{3}}$ là mệnh đề sai vì $P\left( 1 \right)$ là mệnh đề sai.

d. Ta có $\exists x\in N, x>{{x}^{3}}$ là mệnh đề đúng.

<!-- chunk:8 level:3 source:https://toanmath.com/2018/06/cac-dang-toan-ve-menh-de-va-menh-de-chua-bien.html -->
## Ví dụ 7: Dùng các kí hiệu để viết các câu sau và viết mệnh đề phủ định của nó.

a. Tích của ba số tự nhiên liên tiếp chia hết cho $6.$

b. Với mọi số thực bình phương của là một số không âm.

c. Có một số nguyên mà bình phương của nó bằng chính nó.

d. Có một số hữu tỉ mà nghịch đảo của nó lớn hơn chính nó.

a. Mệnh đề $P$: “$\forall n \in N$, $n\left( {n + 1} \right)\left( {n + 2} \right) \vdots 6$” và mệnh đề phủ định $\overline P$: “$\exists n \in N$, $n\left( {n + 1} \right)\left( {n + 2} \right)\not \vdots 6$”.

b. Mệnh đề $Q:$ “$\forall x\in R$, ${{x}^{2}}\ge 0$” và mệnh đề phủ định $\overline{Q}:$ “$\exists x\in R, {{x}^{2}}<0$”.

c. Mệnh đề $R:$ “$\exists n\in Z$, ${{n}^{2}}=n$” và mệnh đề phủ định $\overline{R}:$ “$\forall n\in Z, {{n}^{2}}\ne n$”.

d. Mệnh đề $S:$ “$\exists q\in Q$, $\frac{1}{q}>q$” và mệnh đề phủ định $\overline{S}:$ “$\forall q\in Q, \frac{1}{q}\le q$”.