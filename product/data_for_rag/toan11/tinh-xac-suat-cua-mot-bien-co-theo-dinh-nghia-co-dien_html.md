# Tính xác suất của một biến cố theo định nghĩa cổ điển

<!-- chunk:0 level:0 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-theo-dinh-nghia-co-dien.html -->
Bài viết trình bày phương pháp tính xác suất của một biến cố theo định nghĩa cổ điển, kiến thức và các ví dụ trong bài viết được tham khảo từ các tài liệu chủ đề tổ hợp và xác suất đăng tải trên TOANMATH.com.

1. Định nghĩa cổ điển của xác suất
Giả sử phép thử $T$ có không gian mẫu $Ω$ là một tập hữu hạn và các kết quả của $T$ là đồng khả năng. Nếu $A$ là một biến cố liên quan đến phép thử $T$ và $Ω_A$ là tập hợp các kết quả thuận lợi cho $A$ thì xác suất của $A$ là một số, kí hiệu là $P(A)$, được xác định bởi công thức: $P(A) = \frac{{\left| {{\Omega _A}} \right|}}{{|\Omega |}}.$

Như vậy, việc tính xác suất của biến cố $A$ trong trường hợp này được quy về việc đếm số kết quả có thể của phép thử $T$ và số kết quả thuận lợi cho $A.$

Chú ý: Từ định nghĩa trên ta suy ra:

$0 ≤ P(A) ≤ 1.$

$P(Ω) = 1$, $P(Ø) = 0.$

2. Phương pháp tính xác suất của một biến cố theo định nghĩa cổ điển
+ Xác định không gian mẫu $Ω$, tính $|Ω|.$

+ Xác định biến cố $A$, tính $|Ω_A|.$

+ Tính xác suất theo công thức: $P(A) = \frac{{\left| {{\Omega _A}} \right|}}{{|\Omega |}}.$

3. Ví dụ minh họa

<!-- chunk:1 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-theo-dinh-nghia-co-dien.html -->
## Ví dụ 1.

a) Gieo liên tiếp ba lần con súc sắc. Tìm xác suất của biến cố tổng số chấm không nhỏ hơn $16.$

b) Xếp ngẫu nhiên $5$ chữ cái $B$, $G$, $N$, $O$, $O$. Tìm xác suất để được chữ $BOONG.$

a) Không gian mẫu có $6^3 = 216$ phần tử.

Gọi $A$ là biến cố: “Tổng số chấm không nhỏ hơn $16$”.

Số trường hợp thuận lợi cho $A$ là:

+ Tổng số chấm bằng $18$: có $1$ trường hợp $(6, 6, 6).$

+ Tổng số chấm bằng $17$: có $3$ trường hợp $(5, 6, 6)$, $(6, 5, 6)$, $(6, 6, 5).$

+ Tổng số chấm bằng $16$: có $6$ trường hợp $(6, 6, 4)$, $(6, 4, 6)$, $(4, 6, 6)$, $(6, 5, 5)$, $(5, 5, 6)$, $(5, 6, 5).$

Tổng cộng có $10$ trường hợp thuận lợi cho $A.$

Suy ra: $P(A) = \frac{{10}}{{216}} = \frac{5}{{108}}.$

b) Nếu coi hai chữ cái $O$ là $O_1$ và $O_2$ thì:

Số trường hợp có thể xảy ra là $5! = 120.$

Gọi $B$ là biến cố: “Xếp được chữ $BOONG$”.

Số trường hợp có thể xảy ra $B$ là $2$, gồm $BO_1O_2NG$ và $BO_2O_1NG.$

Suy ra: $P(B) = \frac{2}{{120}} = \frac{1}{{60}}.$

<!-- chunk:2 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-theo-dinh-nghia-co-dien.html -->
## Ví dụ 2. Gieo một con súc sắc cân đối và đồng chất. Giả sử con súc sắc xuất hiện mặt $b$ chấm. Xét phương trình $x^2 + bx + 2 = 0.$ Tính xác suất sao cho:

a) Phương trình có nghiệm.

b) Phương trình vô nghiệm.

c) Phương trình có nghiệm nguyên.

Không gian mẫu có sáu kết quả đồng khả năng: $Ω = \{1, 2, …, 6\}$, $|Ω| = 6.$

Kí hiệu $A$, $B$, $C$ lần lượt là các biến cố tương ứng với các câu hỏi a, b, c.

Phương trình bậc hai $x^2 + bx + 2 = 0$ có biệt thức $\Delta = {b^2} – 8.$

a) $A = \{b ∈ Ω|b^2 – 8 ≥ 0\} = \{3, 4, 5, 6\}$, $|Ω_A| = 4.$

Vậy: $P(A) = \frac{{\left| {{\Omega _A}} \right|}}{{|\Omega |}} = \frac{4}{6} = \frac{2}{3}.$

b) Phương trình vô nghiệm khi và chỉ khi $b∈\{1,2\}.$

Suy ra: $\left| {{\Omega _B}} \right| = 2.$

Vậy: $P(B) = \frac{2}{6} = \frac{1}{3}.$

c) Phương trình có nghiệm khi và chỉ $b = 3.$

Suy ra: $|Ω_C|=1.$

Vậy: $P(C) = \frac{{\left| {{\Omega _c}} \right|}}{{|\Omega |}} = \frac{1}{6}.$

<!-- chunk:3 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-theo-dinh-nghia-co-dien.html -->
## Ví dụ 3. Một bình chứa $8$ viên bi chỉ khác nhau về màu sắc trong đó có $5$ viên bi xanh, $3$ viên bi đỏ. Lấy ngẫu nhiên $2$ viên bi từ bình. Tính xác suất để được:

a) $2$ viên bi xanh.

b) $2$ viên bi đỏ.

Tổng số viên bi có trong bình là $8$ viên, lấy ngẫu nhiên $2$ viên bi, vậy không gian mẫu có: $C_8^2 = 28$ phần tử.

a) Gọi $A$ là biến cố: “Lấy được $2$ viên bi xanh”, ta có: $C_5^2 = 10$ cách lấy.

Vậy $P(A) = \frac{{10}}{{28}} = \frac{5}{{14}}.$

b) Gọi $B$ là biến cố: “Lấy được $2$ viên bi đỏ”, ta có: $C_3^2 = 3$ cách lấy.

Vậy $P(B) = \frac{3}{{28}}.$

<!-- chunk:4 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-theo-dinh-nghia-co-dien.html -->
## Ví dụ 4. Một bình đựng $7$ viên bi chỉ khác nhau về màu sắc, trong đó có $4$ viên bi xanh và $3$ viên bi đỏ. Lấy ngẫu nhiên $3$ viên bi. Tính xác suất để được:

a) $2$ viên bi màu đỏ và $1$ viên bi màu xanh.

b) Cả $3$ viên bi đều màu xanh.

Tổng số có $7$ viên bi, lấy ngẫu nhiên $3$ viên, do đó không gian mẫu có: $C_7^3 = \frac{{7!}}{{3!4!}} = 35$ phần tử.

a) Gọi $A$ là biến cố “Lấy được $2$ viên bi màu đỏ và $1$ viên bi màu xanh”.

Ta có:

$C_3^2 = 3$ cách lấy $2$ viên bi đỏ từ $3$ viên bi đỏ.

$C_4^1 = 4$ cách lấy $1$ viên bi xanh từ $4$ viên bi xanh.

Suy ra $A$ có $3.4 = 12$ phần tử.

Vậy $P(A) = \frac{{12}}{{35}}.$

b) Gọi $B$ là biến cố “Cả ba viên bi cùng màu xanh”.

Ta có: $C_4^3 = 4$ cách lấy $3$ viên bi xanh từ $4$ viên bi xanh.

Suy ra $B$ có $4$ phần tử.

Vậy $P(B) = \frac{4}{{35}}.$

<!-- chunk:5 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-theo-dinh-nghia-co-dien.html -->
## Ví dụ 5. Có $6$ quả cầu giống hệt nhau được đánh số từ $1$ đến $6$ và đựng trong một hộp. Sau khi xáo trộn, người ta lấy ngẫu nhiên lần lượt $4$ quả.

a) Sắp xếp chúng theo thứ tự lấy ra thành một hàng ngang từ trái sang phải. Tìm xác suất để được số $1234.$

b) Tìm xác suất để được tổng các chữ số là $10.$

a) Trong $6$ quả cầu lấy lần lượt $4$ quả.

Ta có:

$6$ cách lấy quả thứ nhất.

$5$ cách lấy quả thứ hai.

$4$ cách lấy quả thứ ba.

$3$ cách lấy quả thứ tư.

Suy ra: không gian mẫu $Ω$ có: $6.5.4.3 = 360$ phần tử.

Trong $360$ phần tử đó chỉ có $1$ phần tử duy nhất mang số $1234.$

Vậy xác suất để được số $1234$ là $\frac{1}{{360}}.$

b) Tổng số $4$ chữ số là $10$ thì các chữ số chỉ có thể là: $1$, $2$, $3$, $4$.

Do đó mỗi số có tổng các chữ số là $10$, là một hoán vị của $4$ chữ số $1$, $2$, $3$, $4.$

Suy ra có $4! = 24$ số có tổng các chữ số là $10.$

Vậy xác suất để được tổng các chữ số là $10$ là: $P = \frac{{24}}{{360}} = \frac{1}{{15}}.$

<!-- chunk:6 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-theo-dinh-nghia-co-dien.html -->
## Ví dụ 6. Cho $8$ quả cân có trọng lượng lần lượt là $1$ kg, $2$ kg, $3$ kg, $4$ kg, $5$ kg, $6$ kg, $7$ kg, $8$ kg. Chọn ngẫu nhiên $3$ quả cân trong số đó.

a) Có bao nhiêu cách chọn như thế.

b) Tính xác suất để trọng lượng $3$ quả cân được chọn không vượt quá $9$ kg.

a) Tổng số là $8$ quả cân, chọn ngẫu nhiên $3$ quả. Vậy ta có: $C_8^3 = \frac{{8!}}{{3!5!}} = 56$ cách chọn.

b) Có $7$ trường hợp để trọng lượng $3$ quả cân không vượt quá $9$ kg là: $(1, 2, 3)$, $(1, 2, 4)$, $(1, 2, 5)$, $(1, 2, 6)$, $(1, 3, 4)$, $(1, 3, 5)$, $(2, 3, 4)$.

Vậy xác suất để biến cố “Trọng lượng $3$ quả cân được chọn không quá $9$ kg” là: $P = \frac{7}{{56}} = \frac{1}{8}.$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-theo-dinh-nghia-co-dien.html -->
## Ví dụ 7. Chọn ngẫu nhiên một số có $3$ chữ số. Tìm xác suất để số được chọn là số chẵn và các chữ số của nó đều khác nhau.

Không gian mẫu $Ω$ là tập hợp các số có dạng $\overline {abc}$ với $a ≠ 0$, $b$, $c$ bất kỳ.

Ta có:

$9$ cách chọn $a$ từ các chữ số $\{1, 2, 3, 4, 5, 6, 7, 8, 9\}.$

$10$ cách chọn $b$ từ các chữ số $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}.$

$10$ cách chọn $c$ từ các chữ số $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}.$

Vậy không gian mẫu $Ω$ có $9.10.10 = 900$ phần tử.

Gọi $M$ là số chẵn và các chữ số của nó khác nhau.

+ Trường hợp 1: Nếu $c = 0$, ta có $9$ cách chọn $b$ và $8$ cách chọn $a.$

Suy ra có $9.8 = 72$ số $M$ với tận cùng bằng $0.$

+ Trường hợp 2: Nếu $c ≠ 0$ $⇒ c ∈ \{2, 4, 6, 8\}$, nên có $4$ cách chọn $c.$

Vì $a ≠ 0$ nên có $8$ cách chọn $a$ và $8$ cách chọn $b.$

Suy ra có $4.8.8 = 256$ số $M$ tận cùng bằng $2$, $4$, $6$, $8.$

Vậy có tất cả $256 + 72 = 328$ số $M$.

Do đó xác suất để biến cố xảy ra là: $P = \frac{{328}}{{900}} = \frac{{82}}{{225}}.$

[ads]

<!-- chunk:8 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-theo-dinh-nghia-co-dien.html -->
## Ví dụ 8. Có $6$ khách hàng vào một cửa hàng gồm $3$ quầy để mua hàng. Tìm xác suất để có $2$ khách hàng vào cùng một quầy.

Gọi $x$ là số khách vào quầy $I$, $y$ là số khách vào quầy $II$, $z$ là số khách vào quầy $III.$

Vậy không gian mẫu $Ω$ là tập hợp các cặp thứ tự $(x;y;z)$ với $x + y + z = 6.$

Ta có:

+ Các số $\{6;0;0\}$, ta có $3$ bộ thứ tự $(6;0;0)$, $(0;6;0)$ và $(0;0;6).$

+ Các số $\{3;3;0\}$, ta có $3$ bộ thứ tự $(3;3;0)$, $(3;0;3)$ và $(0;3;3).$

+ Các số $\{4;1;1\}$, ta có $3$ bộ thứ tự $(4;1;1)$, $(1;4;1)$ và $(1;1;4).$

+ Các số $\{5;1;0\}$, $\{3;2;1\}$, $\{4;2;0\}$ mỗi bộ ta có $3!$ bộ thứ tự.

+ Các số $\{2;2;2\}$, ta có $1$ bộ thứ tự $(2,2,2).$

Vậy không gian mẫu $Ω$ có tất cả: $(3.3) + (3.3!) + 1 = 9 + 18 + 1 = 28$ phần tử, trong đó có các bộ thứ tự có chứa số $2$ là: $(2; 2; 2)$, $(4; 2; 0)$, $(4; 0; 2)$, $(0; 4; 2)$, $(0; 2; 4)$, $(2; 4; 0)$, $(2; 0; 4)$, $(3; 2; 1)$, $(3; 1; 2)$, $(1; 2; 3)$, $(1; 3;2)$, $(2; 1; 3)$ có tất cả $13$ phần tử.

Vậy xác suất để có hai khách hàng vào một quầy là: $P = \frac{{13}}{{28}}.$

<!-- chunk:9 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-theo-dinh-nghia-co-dien.html -->
## Ví dụ 9. Một đợt xổ số phát hành $20000$ vé trong đó có $1$ giải nhất, $100$ giải nhì, $200$ giải ba, $1000$ giải tư và $5000$ giải khuyến khích. Tìm xác suất để một người mua $3$ vé, trúng $1$ giải nhì, $2$ giải khuyến khích.

Tổng số vé là $20000$ vé, mua $3$ vé ngẫu nhiên, suy ra không gian mẫu có: $C_{20000}^3 = 2666266680000.$

Ta có $C_{100}^1 = 100$ cách trúng giải nhì và $C_{5000}^2 = 12497500$ cách trúng giải khuyến khích.

Do đó biến cố “Mua $3$ vé, trúng $1$ giải nhì, $2$ giải khuyến khích” có: $100.12497500 = 1249750000$ cách xảy ra.

Vậy xác suất để một người mua $3$ vé, trúng $1$ giải nhì và $2$ giải khuyến khích là: $\frac{{124975}}{{266626668}} \approx 0,000468.$

<!-- chunk:10 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-theo-dinh-nghia-co-dien.html -->
## Ví dụ 10. Ngân hàng đề thi gồm $100$ câu hỏi. Mỗi đề thi có $5$ câu. Một học sinh thuộc $80$ câu. Tìm xác suất để học sinh đó rút ngẫu nhiên được một đề thi trong đó có $4$ câu hỏi mình đã học thuộc.

Ngân hàng đề thi gồm $100$ câu hỏi, rút ngẫu nhiên $5$ câu hỏi để thành lập một đề thi. Vậy không gian mẫu có: $C_{100}^5 = 75287520$ đề thi.

Gọi $A$ là biến cố “Đề thi gồm $4$ câu đã học thuộc và $1$ câu không thuộc”.

Ta có:

$C_{80}^4= 1581580$ cách chọn $4$ câu đã học thuộc trong số $80$ câu đã học thuộc.

$C_{20}^1 = 20$ cách chọn $1$ câu không thuộc trong số $20$ câu không thuộc.

Suy ra $A$ có $1581580.20 = 31631600$ phần tử.

Vậy $P(A) = \frac{{31631600}}{{75287520}} \approx 0,42.$

<!-- chunk:11 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-theo-dinh-nghia-co-dien.html -->
## Ví dụ 11. Một lô hàng có $10$ sản phẩm, trong đó có $2$ phế phẩm. Lấy tùy ý $6$ sản phẩm từ lô hàng đó. Hãy tìm xác suất để trong $6$ sản phẩm lấy ra có không quá $1$ phế phẩm.

Lấy $6$ sản phẩm từ lô $10$ sản phẩm nên có: $|\Omega | = C_{10}^6 = 210$ trường hợp.

Gọi $A$ là biến cố trong $6$ sản phẩm lấy ra có không quá $1$ phế phẩm.

Suy ra số trường hợp thuận lợi của $A$ là: $\left| {{\Omega _A}} \right| = C_8^6 + C_8^5 \cdot C_2^1$ $= 28 + 112 = 140.$

Suy ra: $P(A) = \frac{{\left| {{\Omega _A}} \right|}}{{|\Omega |}} = \frac{{140}}{{210}} = \frac{2}{3}.$

<!-- chunk:12 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-theo-dinh-nghia-co-dien.html -->
## Ví dụ 12. Có $5$ đoạn thẳng có chiều dài lần lượt là $1$cm, $3$cm, $5$cm, $7$cm và $9$cm. Tính xác suất để khi lấy ngẫu nhiên $3$ đoạn thẳng trong $5$ đoạn thẳng trên, có thể lập thành một tam giác.

Lấy $3$ đoạn thẳng trong $5$ đoạn thẳng (không kể thứ tự) là một tổ hợp chập $3$ của $5$ phần tử. Vậy, số trường hợp đồng khả năng xảy ra là: $|\Omega | = C_5^3 = 10.$

Gọi $A$ là biến cố: “$3$ đoạn thẳng lấy ra tạo nên một tam giác”.

Ta đã biết $a, b, c > 0$ là $3$ cạnh của một tam giác khi: $a + b > c > |a – b|.$

Do đó, từ các đoạn thẳng $1$, $3$, $5$, $7$, $9$ chỉ có những bộ sau đây tạo thành một tam giác: $(3; 5; 7)$, $(3; 7; 9)$, $(5; 7; 9).$

Suy ra: $\left| {{\Omega _A}} \right| = 3.$

Vậy xác suất cần tìm là: $P(A) = \frac{{\left| {{\Omega _A}} \right|}}{{|\Omega |}} = \frac{3}{{10}} = 0,3.$

<!-- chunk:13 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-theo-dinh-nghia-co-dien.html -->
## Ví dụ 13. Cho một lục giác đều $ABCDEF.$ Viết các chữ cái $A$, $B$, $C$, $D$, $E$, $F$ vào sáu cái thẻ. Lấy ngẫu nhiên hai thẻ. Tìm xác suất sao cho đoạn thẳng mà các đầu mút là các điểm được ghi trên hai thẻ đó là:

a) Cạnh của lục giác.

b) Đường chéo của lục giác.

c) Đường chéo nối hai đỉnh đối diện của lục giác.

Không gian mẫu gồm các tổ hợp chập $2$ của $6$ (đỉnh), do đó: $|\Omega | = C_6^2 = 15.$

Kí hiệu $A$, $B$, $C$ là ba biến cố cần tìm xác suất tương ứng các câu hỏi a, b, c.

a) Vì số cạnh của lục giác là $6$ nên: $\left| {{\Omega _A}} \right| = 6$, $P(A) = \frac{{\left| {{\Omega _A}} \right|}}{{|\Omega |}} = \frac{6}{{15}} = \frac{2}{5}.$

b) Số đường chéo là: $\left| {{\Omega _B}} \right| = C_6^2 – 6 = 9.$

Vậy $P(B) = \frac{{\left| {{\Omega _B}} \right|}}{{|\Omega |}} = \frac{9}{{15}} = \frac{3}{5}.$

c) $\left| {{\Omega _C}} \right| = 3$, $P(C) = \frac{{\left| {{\Omega _C}} \right|}}{{|\Omega |}} = \frac{3}{{15}} = \frac{1}{5}.$

<!-- chunk:14 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-theo-dinh-nghia-co-dien.html -->
## Ví dụ 14. Có một hình lập phương mà các mặt của nó đã được sơn màu. Ta cưa ra thành $1000$ khối lập phương nhỏ như nhau. Xác định xác suất để khi lấy ngẫu nhiên ra một khối nhỏ, khối đó có hai mặt đã được sơn màu.

Khi cưa thành $1000$ khối nhỏ, ta thấy $1000$ khối nhỏ đó được chia làm $4$ loại:

+ Khối đỉnh (có $3$ mặt được sơn) gồm $8$ khối.

+ Khối cạnh (có $2$ mặt được sơn) dọc theo $12$ cạnh, mỗi cạnh có $8$ khối thành ra có $96$ khối.

+ Khối mặt (có $1$ mặt được sơn) gồm $6$ mặt, mỗi mặt có $8^2$ khối thành ra có $6.8^2$ khối.

+ Khối ruột (có $0$ mặt được sơn) gồm $8^3$ khối.

Lấy ngẫu nhiên $1$ từ $1000$ khối giống nhau thì số trường hợp đồng khả năng có thể xảy ra là: $|Ω| = 1000.$

Đặt $A$ là biến cố: “Lấy được khối có $2$ mặt được sơn màu”.

Từ phân tích trên ta thấy số trường hợp thuận lợi cho $A$ là $|Ω_A| = 96.$

Vậy: $P(A) = \frac{{\left| {{\Omega _A}} \right|}}{{|\Omega |}} = \frac{{96}}{{1000}} = 0,096.$

<!-- chunk:15 level:3 source:https://toanmath.com/2018/09/tinh-xac-suat-cua-mot-bien-co-theo-dinh-nghia-co-dien.html -->
## Ví dụ 15. Một lô hàng có $n$ sản phẩm trong đó có $m$ sản phẩm xấu. Lấy ngẫu nhiên ra $k$ sản phẩm. Tìm xác suất sao cho trong $k$ sản phẩm lấy ra có $s$ sản phẩm xấu $(s<k).$

Số cách chọn $k$ sản phẩm trong $n$ sản phẩm là $C_n^k.$

Số trường hợp thuận lợi: Lấy $s$ sản phẩm xấu trong $m$ sản phẩm xấu là $C_m^s$ ghép với số cách lấy $k- s$ sản phẩm tốt trong $n – m$ sản phẩm tốt là $C_{n-m}^{k-s}.$

Vậy $P = \frac{{C_m^s.C_{n – m}^{k – s}}}{{C_n^k}}.$