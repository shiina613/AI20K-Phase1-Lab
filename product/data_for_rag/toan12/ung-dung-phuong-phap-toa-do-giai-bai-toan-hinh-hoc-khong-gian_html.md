# Ứng dụng phương pháp tọa độ giải bài toán hình học không gian

<!-- chunk:0 level:0 source:https://toanmath.com/2019/04/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian.html -->
TOANMATH.com giới thiệu đến đọc giả bài viết **ứng dụng phương pháp tọa độ giải bài toán hình học không gian **thuộc chương trình Hình học 12 chương 3.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/04/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian.html -->
## A. PHƯƠNG PHÁP GIẢI TOÁN
1. Phương pháp tổng quát: Để giải một bài toán hình học không gian tổng hợp bằng phương pháp tọa độ, ta thực hiện theo các bước sau:

Bước 1: Chọn hệ trục tọa $Oxyz.$

Xác định ba đường thẳng đồng quy và đôi một cắt nhau trên cơ sở có sẵn của hình (như tam diện vuông, hình hộp chữ nhật, hình chóp tứ giác đều …), hoặc dựa trên các mặt phẳng vuông góc dựng thêm đường phụ.

Bước 2: Tọa độ hóa các điểm của hình không gian.

Tính tọa độ điểm liên quan trực tiếp đến giả thiết và kết luận của bài toán. Cơ sở tính toán chủ yếu dựa vào quan hệ song song, vuông góc cùng các dữ liệu của bài toán.

Bước 3: Chuyển giả thiết qua hình học giải tích.

Lập các phương trình đường, mặt liên quan. Xác định tọa độ các điểm, véc tơ cần thiết cho kết luận.

Bước 4: Giải quyết bài toán.

Sử dụng các kiến thức hình học giải tích để giải quyết yêu cầu của bài toán hình không gian.

Chú ý các công thức về góc, khoảng cách, diện tích và thể tích …

2. Cách chọn hệ tọa độ một số hình không gian
a. Hình hộp lập phương – Hình hộp chữ nhật $ABCD.A’B’C’D’.$

**
<img link="data_for_rag/toan12/images/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian-1.png" alt="">
**

+ Với hình lập phương:

Chọn hệ trục tọa độ sao cho: $A(0;0;0)$, $B(a;0;0)$, $C(a;a;0)$, $D(0;a;0)$, $A'(0;0;a)$, $B'(a;0;a)$, $C'(a;a;a)$, $D'(0;a;a).$

+ Với hình hộp chữ nhật:

Chọn hệ trục tọa độ sao cho: $A(0;0;0)$, $B(a;0;0)$, $C(a;b;0)$, $D(0;b;0)$, $A'(0;0;c)$, $B'(a;0;c)$, $C'(a;b;c)$, $D'(0;b;c).$

Chú ý: Tam diện vuông là một nửa của hình hộp chữ nhật nên ta chọn hệ trục tọa độ tương tự như hình hộp chữ nhật.

b. Với hình hộp đứng có đáy là hình thoi $ABCD.A’B’C’D’.$

<img link="data_for_rag/toan12/images/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian-2.png" alt="">

Chọn hệ trục tọa độ sao cho:

Gốc tọa độ trùng với giao điểm $O$ của hai đường chéo của hình thoi $ABCD.$

Trục $Oz$ đi qua $2$ tâm của $2$ đáy.

Nếu $AC=a$, $BD=b$, $AA’=c$ thì: $A\left( 0;-\frac{a}{2};0 \right)$, $B\left( \frac{b}{2};0;0 \right)$, $C\left( 0;\frac{a}{2};0 \right)$, $D\left( -\frac{b}{2};0;0 \right)$, $A’\left( 0;-\frac{a}{2};c \right)$, $B’\left( \frac{b}{2};0;c \right)$, $C’\left( 0;\frac{a}{2};c \right)$, $D’\left( -\frac{b}{2};0;c \right).$

Chú ý: Với lăng trụ đứng $ABC.A’B’C’$ có đáy $ABC$ là tam giác cân tại $B$ thì ta chọn hệ tọa độ tương tự như trên với gốc tọa độ là trung điểm $AC$, $B\in Ox$, $C\in Oy$ còn trục $Oz$ đi qua trung điểm hai cạnh $AC$, $A’C’.$

c. Hình chóp đều.
+ Hình chóp tam giác đều $S.ABC$, $AB=a$, $SH=h$, ta chọn hệ tọa độ sao cho $O$ là trung điểm $BC$, $A\in Ox$, $B\in Oy.$

Khi đó $A\left( \frac{a\sqrt{3}}{2};0;0 \right)$, $B\left( 0;\frac{a}{2};0 \right)$, $C\left( 0;-\frac{a}{2};0 \right)$, $S\left( \frac{a\sqrt{3}}{6};0;h \right).$

<img link="data_for_rag/toan12/images/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian-3.png" alt="">

+ Hình chóp từ giác đều $S.ABCD$, $AB=a$, $SH=h$, ta chọn hệ tọa độ sao cho $O$ là tâm đáy $B\in Ox$, $C\in Oy$, $S\in Oz$. Khi đó: $A\left( 0;-\frac{a\sqrt{2}}{2};0 \right)$, $B\left( \frac{a\sqrt{2}}{2};0;0 \right)$, $C\left( 0;\frac{a\sqrt{2}}{2};0 \right)$, $D\left( -\frac{a\sqrt{2}}{2};0;0 \right)$, $S\left( 0;0;h \right).$

<img link="data_for_rag/toan12/images/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian-4.png" alt="">

Chú ý: Ngoài cách chọn hệ trục như trên ta có thể chọn hệ trục bằng cách khác.

Chẳng hạn với hình chóp tam giác đều ta có thể chọn $H\equiv O$, trục $Oy$ đi qua $H$ và song song với $BC.$

d. Hình chóp $S.ABCD$ có $SA\bot (ABCD)$, $SA=h.$
+ Nếu đáy là hình chữ nhật ta chọn hệ trục sao cho $A\equiv O$, $B\in Ox$, $D\in Oy$, $S\in Oz.$

<img link="data_for_rag/toan12/images/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian-5.png" alt="">

+ Nếu đáy là hình thoi, ta chọn hệ trục sao cho $O$ là tâm của đáy, $B\in Ox$, $C\in Oy$ và $Oz//SA.$

<img link="data_for_rag/toan12/images/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian-6.png" alt="">

Chú ý: Cho hình chóp $S.ABC$ có $SA\bot (ABC).$

+ Nếu đáy $ABC$ là tam giác vuông tại $A$ thì cách chọn hệ trục hoàn toàn tương tự như hình chóp $S.ABCD$ có đáy là hình chữ nhật.

+ Nếu đáy $ABC$ là tam giác cân tại $B$ thì ta chọn hệ trục tọa độ như hình chóp $S.ABCD$ có đáy là hình thoi, khi đó gốc tọa độ là trung điểm cạnh $AC.$

e. Hình chóp $S.ABC$ có $(SAB)\bot (ABC).$
Đường cao $SH=h$ của tam giác $SAB$ là đường cao của hình chóp.

Nếu tam giác $ABC$ vuông tại $A$, $AB=a$, $AC=b$ ta chọn hệ trục sao cho $A\equiv O$, $B\in Oy$, $C\in Ox$, $Oz//SH$. Khi đó $A\left( 0;0;0 \right)$, $B\left( 0;a;0 \right)$, $C(b;0;0)$, $AH=c$ $\Rightarrow H\left( 0;c;0 \right)$, $S(0;c;h).$

<img link="data_for_rag/toan12/images/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian-7.png" alt="">

Chú ý:

+ Nếu vuông tại $B$ ta chọn $B\equiv O$, vuông tại $C$ chọn $C\equiv O.$

+ Nếu tam giác $ASB$ cân tại $S$, $\Delta ABC$ cân tại $C$ thì ta chọn $H\equiv O$, $C\in Ox$, $B\in Oy$, $S\in Oz.$

Tùy vào từng bài toán mà có thể thay đổi linh hoạt cách chọn hệ tọa độ. Trong nhiều trường hợp, phải biết kết hợp kiến thức hình không gian tổng hợp và kiến thức hình giải tích nhằm thu gọn lời giải.

<!-- chunk:2 level:3 source:https://toanmath.com/2019/04/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian.html -->
## Ví dụ 1. Cho hình chóp $O.ABC$ có $OA=a$, $OB=b$, $OC=c$ đôi một vuông góc. Điểm $M$ cố định thuộc tam giác $ABC$ có khoảng cách lần lượt đến các $mp\left( OBC \right)$, $mp\left( OCA \right)$, $mp\left( OAB \right)$ là $1$, $2$, $3$. Tính $a$, $b$, $c$ để thể tích $O.ABC$ nhỏ nhất.

<img link="data_for_rag/toan12/images/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian-8.png" alt="">

Chọn hệ trục tọa độ như hình vẽ, ta có: $O(0;0;0)$, $A(a;0;0)$, $B(0;b;0)$, $C(0;0;c).$

Vì khoảng cách từ $M$ đến các mặt phẳng $mp\left( OBC \right)$, $mp\left( OCA \right)$, $mp\left( OAB \right)$ là $1$, $2$, $3$ nên $M\left( 1;2;3 \right)$.

Suy ra phương trình $(ABC):\frac{x}{a}+\frac{y}{b}+\frac{z}{c}=1.$

Vì $M\in (ABC)$ $\Rightarrow \frac{1}{a}+\frac{2}{b}+\frac{3}{c}=1$ $(*).$

Thể tích khối chóp $O.ABC$: ${{V}_{O.ABC}}=\frac{1}{6}abc.$

Từ $(*)$ $\Rightarrow 1=\frac{1}{a}+\frac{2}{b}+\frac{3}{c}\ge 3\sqrt[3]{\frac{1}{a}.\frac{2}{b}.\frac{3}{c}}$ $\Rightarrow \frac{1}{6}abc\ge 27.$

Vậy $\min {{V}_{OABC}}=27$ đạt được khi $\frac{1}{a}=\frac{2}{b}=\frac{3}{c}=\frac{1}{3}$ $\Leftrightarrow a=3$, $b=6$, $c=9.$

<!-- chunk:3 level:3 source:https://toanmath.com/2019/04/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian.html -->
## Ví dụ 2. Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $2a$, $SA=a$, $SB=a\sqrt{3}$ và mặt phẳng $(SAB)$ vuông góc với mặt phẳng đáy. Gọi $M$, $N$ lần lượt là trung điểm của các cạnh $AB$, $BC$. Tính theo $a$ thể tích của khối chóp $S.BMDN$ và tính cosin của góc giữa hai đường thẳng $SM$, $DN.$

<img link="data_for_rag/toan12/images/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian-9.png" alt="">

Gọi $H$ là hình chiếu của $S$ lên $AB$ $\Rightarrow SH\bot (ABCD).$

Ta có: $S{{A}^{2}}+S{{B}^{2}}=A{{B}^{2}}$ $\Rightarrow SA\bot SB$ $\Rightarrow AH=\frac{S{{A}^{2}}}{AB}=\frac{a}{2}$, $SH=\frac{a\sqrt{3}}{2}.$

Chọn hệ trục tọa độ như hình vẽ, ta có tọa độ các điểm: $A\left( 0;0;0 \right)$, $B\left( 2a;0;0 \right)$, $D\left( 0;2a;0 \right)$, $C\left( 2a;2a;0 \right)$, $H\left( \frac{a}{2};0;0 \right)$, $S\left( \frac{a}{2};0;\frac{a\sqrt{3}}{2} \right)$, $M\left( a;0;0 \right)$, $N\left( 2a;a;0 \right).$

Ta có ${{S}_{\Delta ADM}}={{S}_{\Delta CDN}}=\frac{1}{2}a.2a={{a}^{2}}$ $\Rightarrow {{S}_{BNDM}}=4{{a}^{2}}-2{{a}^{2}}=2{{a}^{2}}.$

Thể tích khối chóp $S.BMDN$: $V=\frac{1}{3}SH.{{S}_{BMDN}}=\frac{1}{3}.\frac{a\sqrt{3}}{2}.2{{a}^{2}}=\frac{{{a}^{3}}\sqrt{3}}{3}.$

Vì $\overrightarrow{SM}=\left( \frac{a}{2};0;-\frac{a\sqrt{3}}{2} \right)$, $\overrightarrow{DN}=\left( 2a;-a;0 \right)$ $\Rightarrow \overrightarrow{SM}.\overrightarrow{DN}={{a}^{2}}.$

Vậy $\cos \left( SM,DN \right)=\frac{\left| \overrightarrow{SM}.\overrightarrow{DN} \right|}{SM.DN}$ $=\frac{{{a}^{2}}}{a.\sqrt{5}a}=\frac{\sqrt{5}}{5}.$

<!-- chunk:4 level:3 source:https://toanmath.com/2019/04/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian.html -->
## Ví dụ 3. Trên các tia $Ox$, $Oy$, $Oz$ của góc tam diện vuông $Oxyz$ lần lượt lấy các điểm $A$, $B$, $C$ sao cho $OA=a$, $OB=a\sqrt{2}$, $OC=c$, $(a,c>0)$. Gọi $D$ là đỉnh đối diện với $O$ của hình chữ nhật $AOBD$ và $M$ là trung điểm của đoạn $BC.$ Mặt phẳng $(\alpha )$ qua $A$, $M$ cắt mặt phẳng $(OCD)$ theo một đường thẳng vuông góc với đường thẳng $AM.$

1. Gọi $E$ là giao điểm của $(\alpha )$ với đường thẳng $OC.$ Tính độ dài đoạn thẳng $OE.$

2. Tính tỷ số thể tích của hai khối đa diện được tạo thành khi cắt khối chóp $C.AOBD$ bởi mặt phẳng $(\alpha )$. Tính khoảng cách từ điểm $C$ đến mặt phẳng $(\alpha ).$

<img link="data_for_rag/toan12/images/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian-10.png" alt="">

Chọn hệ trục tọa độ $Oxyz$, sao cho:$O(0;0;0)$, $A(a;0;0)$, $B\left( 0;a\sqrt{2};0 \right)$, $D\left( a;a\sqrt{2};0 \right)$, $C(0;0;c).$

1. Vì $M$ là trung điểm của $BC$ nên $M\left( 0;\frac{a\sqrt{2}}{2};\frac{c}{2} \right).$

$\overrightarrow{OC}(0;0;c)$, $\overrightarrow{OD}\left( a;a\sqrt{2};0 \right)$ $\Rightarrow \left[ \overrightarrow{OC};\overrightarrow{OD} \right]=\left( -ac\sqrt{2};ac;0 \right).$

Một véc tơ pháp tuyến của mặt phẳng $(OCD)$ là $\overrightarrow{{{n}_{OCD}}}=\left( -\sqrt{2};1;0 \right).$

Gọi $F=(\alpha )\cap CD$ thì $EF$ là giao tuyến của $(\alpha )$ với $(OCD)$, ta có $EF\bot AM.$

Vì $\overrightarrow{AM}=\left( -a;\frac{a\sqrt{2}}{2};\frac{c}{2} \right)$ nên $\left[ \overrightarrow{{{n}_{OCD}}},\overrightarrow{AM} \right]=\frac{c}{2}(1;\sqrt{2};0)$, do đó một véc tơ chỉ phương của $EF$ là $\overrightarrow{{{u}_{EF}}}=(1;\sqrt{2};0).$

Ta có $\left[ \overrightarrow{{{u}_{EF}}},\overrightarrow{AM} \right]=\frac{1}{2}\left( c\sqrt{2};-c;3\sqrt{2}a \right)$ nên phương trình mặt phẳng $(\alpha )$ là: $\sqrt{2}cx-cy+3\sqrt{2}az-ac\sqrt{2}=0.$

Do đó $(\alpha )\cap Oz=E\left( 0;0;\frac{c}{3} \right)$ $\Rightarrow OE=\frac{c}{3}.$

2. Ta có $(\alpha )\cap CD=F\left( \frac{2a}{3};\frac{2\sqrt{2}a}{3};\frac{c}{3} \right)$ $\Rightarrow \frac{CF}{CD}=\frac{2}{3}.$

Mà ${{V}_{COADB}}=2{{V}_{CAOD}}=2{{V}_{CBOD}}$ nên $\frac{{{V}_{CEAFM}}}{{{V}_{COADB}}}$ $=\frac{{{V}_{CAEF}}}{2{{V}_{CAOD}}}+\frac{{{V}_{CMEF}}}{2{{V}_{CBOD}}}$ $=\frac{1}{2}\left( \frac{CE}{CO}.\frac{CF}{CD}+\frac{CM}{CB}.\frac{CE}{CO}.\frac{CF}{CD} \right)$ $=\frac{1}{3}.$

Do đó tỷ số thể tích hai khối đa diện được tạo thành khi cắt khối chóp $C.AODB$ bởi mặt phẳng $(\alpha )$ là $\frac{1}{2}$ (hay $2$).

Khoảng cách cần tìm: $d(C,(\alpha ))=\frac{\left| 3\sqrt{2}ac-ac\sqrt{2} \right|}{\sqrt{2{{c}^{2}}+{{c}^{2}}+18{{a}^{2}}}}$ $=\frac{2\sqrt{6}ac}{3\sqrt{{{c}^{2}}+6{{a}^{2}}}}.$

<!-- chunk:5 level:3 source:https://toanmath.com/2019/04/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian.html -->
## Ví dụ 4. Trong không gian $Oxyz$, cho hình hộp chữ nhật $ABCD.A’B’C’D’$ có $A\equiv O$, $B\in Ox$, $D\in Oy$, $A’\in Oz$ và $AB=1$, $AD=2$, $AA’=3.$

1. Tìm tọa độ các đỉnh của hình hộp.

2. Tìm điểm $E$ trên đường thẳng $DD’$ sao cho $B’E\bot A’C.$

3. Tìm điểm $M$ thuộc $A’C$, $N$ thuộc $BD$ sao cho $MN\bot BD$, $MN\bot A’C$. Từ đó tính khoảng cách giữa hai đường thẳng chéo nhau $A’C$ và $BD.$

<img link="data_for_rag/toan12/images/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian-11.png" alt="">

1. Ta có $A(0;0;0)$, $B(1;0;0)$, $D(0;2;0)$, $A'(0;0;3).$

Hình chiếu của $C$ lên $(Oxy)$ là $C$, hình chiếu của $C$ lên $Oz$ là $A$ nên $C\left( 1;2;0 \right).$

Hình chiếu của $B’$, $C’$, $D’$ lên mp$(Oxy)$ và trục $Oz$ lần lượt là các điểm $B$, $C$, $D$ và $A’$ nên $B’\left( 1;0;3 \right)$, $C'(1;2;3)$, $D'(0;2;3).$

2. Vì $E$ thuộc đường thẳng $DD’$ nên $E\left( 0;2;z \right)$, suy ra $\overrightarrow{B’E}=\left( -1;2;z-3 \right).$

Mà $\overrightarrow{A’C}=\left( 1;2;-3 \right)$ nên $B’E\bot A’C$ $\Leftrightarrow \overrightarrow{B’E}.\overrightarrow{A’C}=0$ $\Leftrightarrow -1+4-3\left( z-3 \right)=0$ $\Leftrightarrow z=4.$

Vậy $E\left( 0;2;4 \right)$.

3. Đặt $\overrightarrow{A’M}=x.\overrightarrow{A’C}$; $\overrightarrow{BN}=y.\overrightarrow{BD}.$

Ta có:

$\overrightarrow{AM}=\overrightarrow{AA’}+\overrightarrow{A’M}$ $=\overrightarrow{AA’}+x.\overrightarrow{A’C}$ $=\left( x;2x;3-3x \right)$, suy ra $M\left( x;2x;3-3x \right).$

$\overrightarrow{AN}=\overrightarrow{AB}+\overrightarrow{BN}$ $=\overrightarrow{AB}+y.\overrightarrow{BD}$ $=\left( 1-y;2y;0 \right)$ $\Rightarrow N\left( 1-y;2y;0 \right).$

Theo giả thiết của để bài, ta có:
$$
\left\{ \begin{align}
& \overrightarrow{MN}.\overrightarrow{A’C}=0 \\
& \overrightarrow{MN}.\overrightarrow{BD}=0 \\
\end{align} \right.
$$
 $(*).$

Mà $\overrightarrow{MN}=\left( 1-x-y;2y-2x;3x-3 \right)$, $\overrightarrow{A’C}=\left( 1;2;-3 \right)$, $\overrightarrow{BD}=\left( -1;2;0 \right).$

Khi đó $(*)$ trở thành: 
$$
\left\{ \begin{align}
& 1-x-y+4y-4x-9x+9=0 \\
& -1+x+y+4y-4x=0 \\
\end{align} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{align}
& -14x+3y=-10 \\
& -3x+5y=1 \\
\end{align} \right.
$$
 
$$
\Leftrightarrow \left\{ \begin{align}
& x=\frac{53}{61} \\
& y=\frac{44}{61} \\
\end{align} \right. .
$$

Do đó $M\left( \frac{53}{61};\frac{106}{61};\frac{24}{61} \right)$, $N\left( \frac{17}{61};\frac{88}{61};0 \right).$

Vì $MN$ là đường vuông góc chung của hai đường thẳng $A’C$, $BD.$

$d\left( A’C,BD \right)=MN$ $=\sqrt{{{\left( 1-x-y \right)}^{2}}+{{(2y-2x)}^{2}}+{{(3x-3)}^{2}}}$ $=\frac{6\sqrt{61}}{61}.$

<!-- chunk:6 level:3 source:https://toanmath.com/2019/04/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian.html -->
## Ví dụ 5. Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông cân tại $B$, $AB=BC=2a$; hai mặt phẳng $(SAB)$ và $(SAC)$ cùng vuông góc với mặt phẳng $(ABC).$ Gọi $M$ là trung điểm của $AB$; mặt phẳng $SM$ và song song với $BC$, cắt $AC$ tại $N.$ Biết góc giữa hai mặt phẳng $(SBC)$ và $(ABC)$ bẳng $60^0.$ Tính thể tích khối chóp $S.BCNM$ và khoảng cách giữa hai đường thẳng $AB$ và $SN$ theo $a.$

<img link="data_for_rag/toan12/images/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian-12.png" alt="">

Vì hai mặt phẳng $(SAB)$ và $(SAC)$ cùng vuông góc với mặt phẳng $(ABC)$ nên suy ra $SA\bot (ABC).$

Chọn hệ trục tọa độ như hình vẽ, đặt $SA=x$, $x>0.$

Vì $MN//BC$ $\Rightarrow N$ là trung điểm cạnh $AC.$

Tọa độ các đỉnh là: $B(0;0;0)$, $A(2a;0;0)$, $C\left( 0;2a;0 \right)$, $S(2a;0;x)$, $M\left( a;0;0 \right)$, $N\left( a;a;0 \right).$

Suy ra $\overrightarrow{BS}=\left( 2a;0;x \right)$, $\overrightarrow{BC}=\left( 0;2a;0 \right)$ $\Rightarrow \left[ \overrightarrow{BS},\overrightarrow{BC} \right]$ $=\left( -2ax;0;4{{a}^{2}} \right).$

Do đó:

$\overrightarrow{n}=\left( x;0;-2a \right)$ là VTPT của mặt phẳng $(SBC).$

$\overrightarrow{k}=(0;0;1)$ là VTPT của mặt phẳng $(ABC).$

Theo giả thiết ta có: $\frac{\left| \overrightarrow{n}.\overrightarrow{k} \right|}{\left| \overrightarrow{n} \right|.\left| \overrightarrow{k} \right|}$ $=\cos {{60}^{0}}=\frac{1}{2}$ $\Leftrightarrow \frac{2a}{\sqrt{{{x}^{2}}+4{{a}^{2}}}}=\frac{1}{2}$ $\Rightarrow {{x}^{2}}=12{{a}^{2}}$ $\Rightarrow x=2a\sqrt{3}.$

Vì $M$, $N$ là trung điểm của $AB$, $CB$ nên: ${{S}_{\Delta AMN}}=\frac{1}{4}{{S}_{\Delta ABC}}$ $\Rightarrow {{S}_{BMNC}}=\frac{3}{4}{{S}_{\Delta ABC}}=\frac{3{{a}^{2}}}{2}.$

Từ đó suy ra thể tích khối chóp $S.BMNC$ là: ${{V}_{S.BMNC}}=\frac{1}{3}SA.{{S}_{BMNC}}$ $=\frac{1}{3}.2a\sqrt{3}.\frac{3{{a}^{2}}}{2}={{a}^{3}}\sqrt{3}.$

Ta có: $\overrightarrow{BA}=\left( 2a;0;0 \right)$, $\overrightarrow{SN}=\left( -a;a;2a\sqrt{3} \right)$, $\overrightarrow{BN}=\left( a;a;0 \right).$

Suy ra $\left[ \overrightarrow{BA},\overrightarrow{SN} \right]=\left( 0;-4\sqrt{3}{{a}^{2}};2{{a}^{2}} \right)$ $\Rightarrow \left[ \overrightarrow{BA},\overrightarrow{SN} \right].\overrightarrow{BN}=-4\sqrt{3}{{a}^{3}}.$

Vậy $d\left( AB,SN \right)=\frac{\left| \left[ \overrightarrow{BA},\overrightarrow{SN} \right].\overrightarrow{BN} \right|}{\left| \left[ \overrightarrow{BA},\overrightarrow{SN} \right] \right|}$ $=\frac{4{{a}^{3}}\sqrt{3}}{2\sqrt{13}{{a}^{2}}}$ $=\frac{2a\sqrt{39}}{13}.$

<!-- chunk:7 level:4 source:https://toanmath.com/2019/04/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian.html -->
## Bài tập 1.

1. Cho hình lập phương $ABCD.A’B’C’D’$ có cạnh bằng $a$. Chứng minh hai đường chéo $B’D’$ và $A’B$ của hai mặt bên là hai đường thẳng chéo nhau. Tìm khoảng cách giữa hai đường thẳng chéo nhau $B’D’$ và $A’B$.

2. Cho hình lăng trụ đứng $ABC.A’B’C’$, có đáy $AB=a$, $AC=2a$, $\widehat{BAC}={{120}^{0}}$. Gọi $M$ là trung điểm cạnh bên $BB’$, biết hai mặt phẳng $(MAC)$ và $(MA’C’)$ vuông góc với nhau. Tính thể tích khối lăng trụ và côsin của góc giữa hai mặt phẳng $(MAC)$ và $(BCC’B’)$.

3. Cho lăng trụ $ABC.A’B’C’$ có độ dài cạnh bên bằng $2a$, đáy $ABC$ là tam giác vuông tại $A$, $AB=a$, $AC=a\sqrt{3}$ và hình chiếu vuông góc của đỉnh $A’$ trên mặt phẳng $(ABC)$ là trung điểm của cạnh $BC$. Tính theo $a$ thể tích khối chóp $A’.ABC$ và tính cosin của góc giữa hai đường thẳng $AA’$, $B’C’.$

4. Cho lăng trụ đứng $ABC.A’B’C’$ có đáy $ABC$ là tam giác vuông, $AB=BC=a$, cạnh bên $AA’=a\sqrt{2}$. Gọi $M$ là trung điểm của cạnh $BC$. Tính theo $a$ thể tích của khối lăng trụ $ABC.A’B’C’$ và khoảng cách giữa hai đường thẳng $AM$, $B’C$.

5. Cho hình lăng trụ tam giác $ABC.A’B’C’$ có $BB’=a$, góc giữa đường thẳng $BB’$ và mặt phẳng $(ABC)$ bằng ${{60}^{0}}$; tam giác $ABC$ vuông tại $C$ và $\widehat{BAC}={{60}^{0}}$. Hình chiếu vuông góc của điểm $B’$ lên mặt phẳng $(ABC)$ trùng với trọng tâm của tam giác $ABC$. Tính thể tích khối tứ diện $A’ABC$ theo $a.$

6. Cho hình lăng trụ đứng $ABC.A’B’C’$ có đáy $ABC$ là tam giác vuông tại $B$, $AB=a$, $AA=2a$, $AC=3a$. Gọi $M$ là trung điểm của đoạn thẳng $A’C’$, $I$ là giao điểm của $AM$ và $A’C$. Tính theo $a$ thể tích khối tứ diện $IABC$ và khoảng cách từ điểm $A$ đến mặt phẳng $\left( IBC \right)$.

7. Cho hình lăng trụ tam giác đều $ABC.A’B’C’$ có $AB=a$, góc giữa hai mặt phẳng $\left( A’BC \right)$ và $\left( ABC \right)$ bằng ${{60}^{0}}$. Gọi $G$ là trọng tâm tam giác $A’BC$. Tính thể tích khối lăng trụ đã cho và tính bán kính mặt cầu ngoại tiếp tứ diện $GABC$ theo $a$.

8. Cho lăng trụ $ABCD.{{A}_{1}}{{B}_{1}}{{C}_{1}}{{D}_{1}}$ có đáy $ABCD$ là hình chữ nhật. $AB=a$, $AD=a\sqrt{3}$. Hình chiếu vuông góc của điểm ${{A}_{1}}$ trên mặt phẳng $\left( ABCD \right)$ trùng với giao điểm $AC$ và $BD$. Góc giữa hai mặt phẳng $\left( AD{{D}_{1}}{{A}_{1}} \right)$ và $\left( ABCD \right)$ bằng ${{60}^{0}}$. Tính thể tích khối lăng trụ đã cho và khoảng cách từ điểm ${{B}_{1}}$ đến mặt phẳng $\left( {{A}_{1}}BD \right)$ theo $a$.

<!-- chunk:8 level:4 source:https://toanmath.com/2019/04/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian.html -->
## Bài tập 2. Cho hình tứ diện $ABCD$ có cạnh $AD$ vuông góc với mặt phẳng $\left( ABC \right)$; $AC=AD=4cm$; $AB=3cm$ và $BC=5cm.$

a) Tính khoảng cách từ điểm $A$ đến mặt phẳng $(BCD).$

b) Gọi $M$, $N$ lần lượt là trung điểm các cạnh $BD$, $BC$. Tính góc và khoảng cách giữa hai đường thẳng $CM$ và $AN$.

<!-- chunk:9 level:4 source:https://toanmath.com/2019/04/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian.html -->
## Bài tập 3.

1. Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình chữ nhật, cạnh bên $SA$ vuông góc với đáy, $AB=a$, $AD=2a$, $SA=3a$. Gọi $M$, $N$ lần lượt là hình chiếu của $A$ lên $SB$, $SD$ và $P$ là giao điểm của $SC$ với mặt phẳng $(AMN)$.

a) Tính thể tích khối chóp $S.AMPN.$

b) Tính khoảng cách và côsin của góc giữa $DM$ và $CN$.

2. Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang vuông tại $A$ và $B$; $AB=AD=2a$; $CB=a$; góc giữa hai mặt phẳng $(SBC)$ và $\left( ABCD \right)$ bằng ${{60}^{0}}$. Gọi $I$ là trung điểm của cạnh $AB$. Biết hai mặt phẳng $\left( SDI \right)$ và $\left( SCI \right)$ cùng vuông góc với mặt phẳng $\left( ABCD \right)$, tính thể tích khối chóp $S.ABCD$ theo $a$.

3. Cho hình chóp $S.ABCD$ có đáy là hình chữ nhật, $AB=a$, $AD=\sqrt{2}a$, $SA=a$ và vuông góc với $mp(ABCD)$. Gọi $M$, $N$ lần lượt là trung điểm của các cạnh $AD$, $SC$. Gọi $I$ là giao điểm của $BM$, $AC$. Chứng minh $mp(SAC)$ vuông góc với $(SMB)$. Tính thể tích của khối tứ diện $ANIB.$

4. Cho hình chóp $S.ABCD$ có đáy là hình vuông cạnh $a$, mặt bên $SAD$ là tam giác đều và nằm trong mặt phẳng vuông góc với đáy. Gọi $M$, $N$, $P$ lần lượt là trung điểm của các cạnh $SB$, $BC$, $CD$. Chứng minh $AM$ vuông góc với $BP$ và tính thể tích khối tứ diện $CMNP$.

5. Cho hình chóp tứ giác đều $S.ABCD$ có đáy là hình vuông cạnh $a$. Gọi $E$ là điểm đối xứng của $D$ qua trung điểm của $SA$. $M$ là trung điểm của $AE$, $N$ là trung điểm của $BC$. Chứng minh $MN$ vuông góc với $BD$ và tính (theo $a$) khoảng cách giữa hai đường thẳng $MN$ và $AC$.

6. Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$. Gọi $M$ và $N$ lần lượt là trung điểm của các cạnh $AB$ và $AD$; $H$ là giao điểm của $CN$ và $DM$. Biết $SH$ vuông góc với mặt phẳng $(ABCD)$ và $SH=a\sqrt{3}$. Tính thể tích khối chóp $S.CDNM$ và khoảng cách giữa hai đường thẳng $DM$ và $SC$ theo $a$.

7. Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh $a$, cạnh bên $SA=a$; hình chiếu vuông góc của đỉnh $S$ trên mặt phẳng $(ABCD)$ là điểm $H$ thuộc đoạn $AC$, $AH=\frac{AC}{4}$. Gọi $CM$ là đường cao của tam giác $SAC$. Chứng minh $M$ là trung điểm của $SA$ và tính thể tích khối tứ diện $SMBC$ theo $a$.

<!-- chunk:10 level:4 source:https://toanmath.com/2019/04/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian.html -->
## Bài tập 4.

1. Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác cân $AB=AC=a$, $\widehat{BAC}={{120}^{0}}$, $SA$ vuông góc với mặt phẳng đáy. Hai mặt phẳng $(SAB)$ và $(SBC)$ tạo với nhau một góc ${{60}^{0}}$. Gọi $M$, $N$ lần lượt là trung điểm của các cạnh $SB$, $SC$. Tính thể tích khối chóp $S.ABC$ và $S.AMN$.

2. Cho hình chóp tam giác đều $S.ABC$ có độ dài cạnh đáy là $a$. Gọi $M$, $N$ là trung điểm $SB$, $SC$. Tính theo $a$ diện tích $\Delta AMN$, biết $(AMN)$ vuông góc với $(SBC)$.

3. Cho hình chóp $S.ABC$ có đáy là tam giác đều cạnh $a$. Cạnh bên $SA=2a$ và vuông góc với $mp(ABC)$. Gọi $M$, $N$ lần lượt là hình chiếu của $A$ lên $SB$, $SC$. Tính thể tích của khối chóp $A.BCMN$.

4. Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông tại $B$, $BA=3a$, $BC=4a$; mặt phẳng $(SBC)$ vuông góc với mặt phẳng $(ABC)$. Biết $SB=2a\sqrt{3}$ và $\widehat{SBC}={{30}^{0}}$. Tính thể tích khối chóp $S.ABC$ và khoảng cách từ điểm $B$ đến mặt phẳng $(SAC)$ theo $a$.

<!-- chunk:11 level:4 source:https://toanmath.com/2019/04/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian.html -->
## Bài tập 5. Cho hình chóp $O.ABC$ có $OA$, $OB$, $OC$ đôi một vuông góc và $OA=a$, $OB=b$, $OC=c.$

1. Chứng minh rằng $OH\bot (ABC)$, $H\in (ABC)$ khi và chỉ khi $H$ là trực tâm của tam giác $ABC.$

2. Tính khoảng cách từ $O$ đến mặt phẳng $(ABC).$

3. Cho $M$ là một điểm bất kỳ trên mặt phẳng $(ABC)$, không trùng với $A$, $B$, $C$, $H$ ($H$ trực tâm tam giác $ABC$). Chứng minh rằng: $\frac{A{{M}^{2}}}{A{{O}^{2}}}$ $+\frac{B{{M}^{2}}}{B{{O}^{2}}}$ $+\frac{C{{M}^{2}}}{C{{O}^{2}}}$ $=2+\frac{H{{M}^{2}}}{H{{O}^{2}}}.$

4. Gọi $\alpha$, $\beta$, $\gamma$ lần lượt là góc giữa các mặt bên với mặt đáy. Chứng minh: $\frac{{{\sin }^{2}}\alpha }{1+\sin \beta \sin \gamma }$ $+\frac{{{\sin }^{2}}\beta }{1+\sin \gamma \sin \alpha }$ $+\frac{{{\sin }^{2}}\gamma }{1+\sin \alpha \sin \beta }$ $\ge \frac{6}{5}.$

<!-- chunk:12 level:4 source:https://toanmath.com/2019/04/ung-dung-phuong-phap-toa-do-giai-bai-toan-hinh-hoc-khong-gian.html -->
## Bài tập 7. Trong không gian với hệ trục tọa độ $Oxyz$ cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang vuông tại $A$, $B$ với $AB=BC=a$; $AD=2a$; $A\equiv O$, $B$ thuộc tia $Ox$, $D$ thuộc tia $Oy$ và $S$ thuộc tia $Oz$. Đường thẳng $SC$ và $BD$ tạo với nhau một góc $\alpha$ thỏa $\cos \alpha =\frac{1}{\sqrt{30}}$.

1. Xác định tọa độ các đỉnh của hình chóp.

2. Chứng minh rằng $\Delta SCD$ vuông, tính diện tích tam giác $SCD$ và tính côsin của góc hợp bởi hai mặt phẳng $(SAB)$ và $(SCD)$.

3. Gọi $E$ là trung điểm cạnh $AD$. Tìm tọa độ tâm và tính bán kính mặt cầu ngoại tiếp hình chóp $S.BCE$.

4. Trên các cạnh $SA$, $SB$, $BC$, $CD$ lần lượt lấy các điểm $M$, $N$, $P$, $Q$ thỏa $SM=MA$, $SN=2NB$, $BP=3PC$, $CQ=4QD$. Chứng minh rằng $M$, $N$, $P$, $Q$ không đồng phẳng và tính thể tích khối chóp $MNPQ$.