# Bài toán trả góp

<!-- chunk:0 level:0 source:https://toanmath.com/2019/12/bai-toan-tra-gop.html -->
Bài viết hướng dẫn phương pháp giải bài toán trả góp, trả nợ, vay vốn … thường gặp trong chương trình Giải tích 12 và đề thi trắc nghiệm THPT Quốc gia môn Toán.

<!-- chunk:1 level:1 source:https://toanmath.com/2019/12/bai-toan-tra-gop.html -->
## A. BÀI TOÁN TỔNG QUÁT TỔNG QUÁT

Một khách hàng vay $a$ đồng với lãi suất $r\%$/tháng. Cứ sau đúng $1$ tháng thì khách hàng trả $m$ đồng. Hỏi sau bao nhiêu tháng thì khách hàng này hết nợ.

<!-- chunk:2 level:1 source:https://toanmath.com/2019/12/bai-toan-tra-gop.html -->
## B. LỜI GIẢI TỔNG QUÁT

Ta tính số tiền còn lại sau $n$ tháng trả nợ:

+ Số tiền còn lại sau tháng thứ nhất là:

${S_1} = a(1 + r) – m.$

+ Số tiền còn lại sau tháng thứ hai là:

${S_2} = [a(1 + r) – m] + [a(1 + r) – m]r – m$ $= a{(1 + r)^2} – m[(1 + r) + 1].$

+ Số tiền còn lại sau tháng thứ ba là:

${S_3} = a{(1 + r)^3}$ $– m\left[ {{{(1 + r)}^2} + (1 + r) + 1} \right].$

… …

+ Số tiền còn lại sau $n$ tháng trả nợ là:

${S_n} = a{(1 + r)^n}$ $– m\left[ {{{(1 + r)}^{n – 1}} + {{(1 + r)}^{n – 2}} + \ldots + (1 + r) + 1} \right].$

$= a{(1 + r)^n} – m.\frac{{{{(1 + r)}^n} – 1}}{r}.$

Để sau $n$ tháng khách hàng trả hết nợ thì:

${S_n} = a{(1 + r)^n} – m.\frac{{{{(1 + r)}^n} – 1}}{r} = 0.$

<!-- chunk:3 level:1 source:https://toanmath.com/2019/12/bai-toan-tra-gop.html -->
## C. BÀI TẬP VẬN DỤNG

## Câu 1. Anh Tài vay ngân hàng $2$ tỉ đồng để xây nhà và trả dần mỗi năm $500$ triệu đồng. Kì trả đầu tiên là sau khi nhận vốn với lãi suất trả chậm $9\%$ một năm. Hỏi sau mấy năm anh Tài mới trả hết nợ đã vay?

A. $5$ năm.

B. $3$ năm.

C. $4$ năm.

D. $6$ năm.

Hướng dẫn giải:

Phân tích và tìm lời giải tổng quát:

Kì trả nợ đầu tiên là sau khi nhận vốn nên đây là bài toán vay vốn trả góp đầu kì.

Gọi $A$ là số tiền vay ngân hàng, $B$ là số tiền trả trong mỗi chu kì, $d = r\%$ là lãi suất trả chậm (tức là lãi suất cho số tiền còn nợ ngân hàng) trên một chu kì, $n$ là số kì trả nợ.

Số tiền còn nợ ngân hàng (tính cả lãi) trong từng chu kì như sau:

+ Đầu kì thứ nhất là $A – B.$

+ Đầu kì thứ hai là $(A – B)(1 + d) – B$ $= A(1 + d) – B[(1 + d) + 1].$

+ Đầu kì thứ ba là $[A(1 + d) – B((1 + d) + 1)](1 + d) – B$ $= A{(1 + d)^2} – B\left[ {{{(1 + d)}^2} + (1 + d) + 1} \right].$

… …

+ Theo giả thiết quy nạp, đầu kì thứ $n$ là:

$A{(1 + d)^{n – 1}}$ $– B\left[ {{{(1 + d)}^{n – 1}} + \ldots + (1 + d) + 1} \right]$ $= A{(1 + d)^{n – 1}} – B\frac{{{{(1 + d)}^n} – 1}}{d}.$

Vậy số tiền còn nợ (tính cả lãi) sau $n$ chu kì là $A{(1 + d)^{n – 1}} – B\frac{{{{(1 + d)}^n} – 1}}{d}.$

Trở lại bài toán đã cho, để sau $n$ năm (chu kì ở đây ứng với một năm) anh Tài trả hết nợ thì ta có:

$A{(1 + d)^{n – 1}} – B\frac{{{{(1 + d)}^n} – 1}}{d} = 0$ $\Leftrightarrow 2.1,{09^{n – 1}} – 0,5.\frac{{1,{{09}^n} – 1}}{{0,09}} = 0$ $\Leftrightarrow n \approx 4,7.$

Vậy phải sau $5$ năm anh Tài mới trả hết nợ đã vay.

> **Đáp án: A**

## Câu 2. Một người vay ngân hàng số tiền $350$ triệu đồng, mỗi tháng trả góp $8$ triệu đồng và lãi suất cho số tiền chưa trả là $0,79\%$ một tháng. Kì trả đầu tiên là cuối tháng thứ nhất. Hỏi số tiền phải trả ở kì cuối là bao nhiêu để người này hết nợ ngân hàng? (làm tròn đến hàng nghìn).

A. $7140000$ đồng.

B. $984000$ đồng.

C. $2944000$ đồng.

D. $2921000$ đồng.

Hướng dẫn giải:

Phân tích và tìm lời giải cho bài toán tổng quát:

Kì trả đầu tiên là cuối tháng thứ nhất nên đây là bài toán vay vốn trả góp cuối kì.

Gọi $A$ là số tiền vay ngân hàng, $B$ là số tiền trả trong mỗi chu kì, $d = r\%$ là lãi suất cho số tiền chưa trả trên một chu kì, $n$ là số kì trả nợ.

Số tiền còn nợ ngân hàng (tính cả lãi) trong từng chu kì được tính như sau:

+ Đầu kì thứ nhất là $A.$

+ Cuối kì thứ nhất là $A(1 + d) – B.$

+ Cuối kì thứ hai là $(A(1 + d) – B)(1 + d) – B$ $= A{(1 + d)^2} – B[(1 + d) + 1].$

+ Cuối kì thứ ba là $\left[ {A{{(1 + d)}^2} – B((1 + d) + 1)} \right](1 + d) – B$ $= A{(1 + d)^3} – B\left[ {{{(1 + d)}^2} + 1(1 + d) + 1} \right].$

… …

+ Theo giả thiết quy nạp, cuối kì thứ $n$ là:

$A{(1 + d)^n}$ $– B\left[ {{{(1 + d)}^{n – 1}} + \ldots + (1 + d) + 1} \right]$ $= A{(1 + d)^n} – B\frac{{{{(1 + d)}^n} – 1}}{d}.$

Vậy số tiền còn nợ (tính cả lãi) sau $n$ chu kì là:

${S_n} = A{(1 + d)^n} – B\frac{{{{(1 + d)}^n} – 1}}{d}.$

Trở lại đề bài, ta gọi $n$ (tháng) là số kì trả hết nợ.

Khi đó, ta có:

$A{(1 + d)^n} – B\frac{{{{(1 + d)}^n} – 1}}{d} = 0$ $\Leftrightarrow 350.1,{0079^n} – 8.\frac{{1,{{0079}^n} – 1}}{{0,0079}} = 0$ $\Leftrightarrow n \approx 53,9.$

Tức là phải mất $54$ tháng người này mới trả hết nợ.

Cuối tháng thứ $53$, số tiền còn nợ (tính cả lãi) là:

${S_{53}} = 350.1,{0079^{53}} – 8.\frac{{1,{{0079}^{53}} – 1}}{{0,0079}}$ (triệu đồng).

Kì trả nợ tiếp theo là cuối tháng thứ $54$, khi đó phải trả số tiền ${S_{53}}$ và lãi của số tiền này nữa là: ${S_{53}}.1,0079 \approx 7,139832$ (triệu đồng).

> **Đáp án: A**

## Câu 3. Theo chính sách tín dụng của chính phủ hỗ trợ sinh viên vay vốn trang trải học tập: mỗi sinh viên được vay tối đa $900 000$ đồng/tháng ($9$ triệu/năm học), với lãi suất $0,45\%$ một tháng. Mỗi năm lập thủ tục vay $2$ lần ứng với $2$ học kì và được nhận tiền vay đầu mỗi học kì (mỗi lần nhận tiền vay là $4,5$ triệu). Giả sử sinh viên A trong thời gian học đại học $5$ năm vay tối đa theo chính sách thì tổng số tiền nợ bao gồm cả lãi là bao nhiêu? (làm tròn đến hàng đơn vị).

A. $52343156$ đồng.

B. $52343155$ đồng.

C. $46128921$ đồng.

D. $96128922$ đồng.

> **Đáp án: A**

## Câu 4. Được sự hỗ trợ từ Ngân hàng Chính sách xã hội địa phương, nhằm giúp đỡ các sinh viên có hoàn cảnh khó khăn hoàn thành việc đóng học phí học tập, một bạn sinh viên A đã vay của ngân hàng $20$ triệu đồng với lãi suất $12\%$/năm và ngân hàng chỉ bắt đầu tính lãi sau khi bạn A kết thúc khóa học. Bạn A đã hoàn thành khóa học và đi làm với mức lương là $5,5$ triệu đồng/tháng. Bạn A dự tính sẽ trả hết nợ gốc lẫn lãi suất cho ngân hàng trong $36$ tháng. Hỏi số tiền $m$ mỗi tháng mà bạn A phải trả cho ngân hàng là bao nhiêu?

A. $m = \frac{{1,{{12}^3} \times 20 \times 0,12}}{{\left( {1,{{12}^3} – 1} \right) \times 12}}$ triệu.

B. $m = \frac{{1,{{12}^3} \times 20 \times 0,12}}{{\left( {1,{{12}^3} – 1} \right) \times 12}}$ triệu.

C. $m = \frac{{1,{{12}^3} \times 36 \times 0,12}}{{\left( {1,{{12}^3} – 1} \right) \times 12}}$ triệu.

D. $m = \frac{{1,{{12}^2} \times 36 \times 0,12}}{{\left( {1,{{12}^2} – 1} \right) \times 12}}$ triệu.

Hướng dẫn giải:

Năm thứ nhất trả gốc và lãi, số tiền còn lại:

${x_1} = (1 + 0,12){x_0} – 12m$ $= 1,12{x_0} – 12m$, ${x_0} = 20$ triệu.

Năm thứ hai, số tiền còn lại:

${x_2} = (1 + 0,12){x_1} – 12m$ $= 1,12{x_1} – 12m.$

Năm thứ ba, số tiền còn lại:

${x_3} = (1 + 12\% ){x_2} – 12m$ $= 1,12{x_2} – 12m = 0.$

$\Rightarrow m = \frac{{1,{{12}^3} \times 20}}{{\left( {1 + 1,12 + 1,{{12}^2}} \right) \times 12}}$ $= \frac{{1,{{12}^3} \times 20}}{{\frac{{1,{{12}^3} – 1}}{{1,12 – 1}} \times 12}}$ $= \frac{{1,{{12}^3} \times 20 \times 0,12}}{{\left( {1,{{12}^2} – 1} \right) \times 12}}.$

$m = \frac{{1,{{12}^3} \times 20 \times 0,12}}{{\left( {1,{{12}^3} – 1} \right) \times 12}}$ triệu.

> **Đáp án: A**

## Câu 5. Một người vay vốn ở một ngân hàng với số tiền là $50$ triệu đồng, thời hạn $48$ tháng, lãi suất $1,15\%$ trên tháng, tính theo dư nợ, trả đúng ngày quy định. Hỏi hằng tháng, người đó phải điều đặn trả một khoản tiền cả gốc lẫn lãi là bao nhiêu để đến tháng thứ $48$ thì người đó trả hết cả gốc lẫn lãi cho ngân hàng?

A. $1616666,667$ đồng.

B. $1361312,807$ đồng.

C. $1561312,208$ đồng.

D. $1461312,208$ đồng.

Hướng dẫn giải:

Sử dụng công thức: ${S_n} = A{(1 + d)^n} – B\frac{{{{(1 + d)}^n} – 1}}{d}.$

Để hết nợ thì ${S_n} = 0$ $\Leftrightarrow B = \frac{{Ad{{(1 + d)}^n}}}{{{{(1 + d)}^n} – 1}}$, với $A$ là số tiền vay ban đầu, $B$ là số tiền trả hằng tháng $d$ là lãi suất vay và $n$ là số tháng trả nợ.

> **Đáp án: B**

## Câu 6. Ông B đến siêu thị điện máy để mua một cái laptop với giá $15,5$ triệu đồng theo hình thức trả góp với lãi suất $2,5\%$/tháng. Để mua trả góp ông B phải trước $30\%$ số tiền, số tiền còn lại ông sẽ trả dần trong thời gian $6$ tháng kể từ ngày mua, mỗi lần trả cách nhau $1$ tháng. Số tiền mỗi tháng ông B phải trả là như nhau và tiền lãi được tính theo nợ gốc còn lại ở cuối mỗi tháng. Hỏi nếu ông B mua theo hình thức trả góp như trên thì số tiền phải trả nhiều hơn so với giá niêm yết là bao nhiêu? Biết rằng lãi suất không đổi trong thời gian ông B hoàn nợ (làm tròn đến chữ số hàng nghìn).

A. $1 628 000$ đồng.

B. $2 325 000$ đồng.

C. $1 384 000$ đồng.

D. $970 000$ đồng.

Hướng dẫn giải:

Số tiền ông B vay trả góp là: $A = 15.500000 – 15500000.0,3$ $= 10850000$ đồng.

Gọi $a$ là số tiền ông B phải trả góp hằng tháng.

+ Hết tháng thứ nhất, số tiền còn nợ là:

${N_1} = A(1 + r) – a.$

+ Hết tháng thứ $2$, số tiền còn nợ là:

${N_2} = {N_1}(1 + r) – a$ $= A{(1 + r)^2} – a(1 + r) – a.$

+ Hết tháng thứ $3$, số tiền còn nợ là:

${N_3} = A{(1 + r)^3} – a{(1 + r)^2}$ $– a(1 + r) – a.$

… …

+ Cuối tháng thứ $n$, số tiền còn nợ là:

${N_n}$ $= A{(1 + r)^n}$ $– a{(1 + r)^{n – 1}}$ $– a{(1 + r)^{n – 2}}$ $– \ldots – a$ $= A{(1 + r)^n} – a.\frac{{{{(1 + r)}^n} – 1}}{r}.$

Để trả hết nợ sau $n$ tháng thì: ${N_n} = 0$ $\Leftrightarrow a = \frac{{Ar{{(1 + r)}^n}}}{{{{(1 + r)}^n} – 1}}.$

$\Rightarrow a = \frac{{10,{{85.10}^6}.0,025{{(1,025)}^6}}}{{{{(1,025)}^6} – 1}}$ $\approx 1970000$ đồng.

Vậy số tiền ông B phải trả nhiều hơn khi mua bằng hình thức trả góp là:

$1970000.6 – 10850000 = 970000$ đồng.

> **Đáp án: D**

## Câu 7. Một anh công nhân được lĩnh lương khởi điểm là $700000$ đồng/tháng. Cứ ba năm anh ta lại được tăng lương thêm $7\% .$ Hỏi sau $36$ năm làm việc anh công nhận được lĩnh tổng cộng bao nhiêu tiền (lấy chính xác đến hàng đơn vị)?

A. $456 788 972$ đồng.

B. $450 788 972$ đồng.

C. $452 788 972$ đồng.

D. $454 788 972$ đồng.

Hướng dẫn giải:

+ Tiền lương $3$ năm đầu: ${T_2} = 36 \times 700$ nghìn.

+ Tiền lương $3$ năm thứ hai: ${T_2} = {T_1} + {T_1} \times 7\%$ $= {T_1}(1 + 7\% ).$

+ Tiền lương $3$ năm thứ ba: ${T_3} = {T_1}(1 + 7\% ) + {T_1}(1 + 7\% ) \times 7\%$ $= {T_1}{(1 + 7\% )^2}.$

+ Tiền lương $3$ năm thứ tư: ${T_4} = {T_1}{(1 + 7\% )^3}.$

… …

+ Tiền lương $3$ năm thứ $12$: ${T_{12}} = {T_1}{(1 + 7\% )^{11}}.$

Tổng tiền lương sau $36$ năm: $T = {T_1} + {T_2} + \ldots + {T_{12}}$ $= \frac{{{u_1}\left( {1 – {q^{12}}} \right)}}{{1 – q}}$ $= \frac{{{T_1}\left[ {1 – {{(1 + 7\% )}^{12}}} \right]}}{{1 – (1 + 7\% )}}$ $= 450788972.$

> **Đáp án: B**

## Câu 8. Giả sử tỉ lệ lạm phát của Việt Nam trong năm 2016 là $2,5\%$ và tỉ lệ này không thay đổi trong $10$ năm tiếp theo. Hỏi nếu năm 2016, giá xăng là $16 000$ VNĐ/lít thì năm 2025 giá tiền xăng là bao nhiêu tiền một lít?

A. $19 600$ VNĐ/lít.

B. $19 981$ VNĐ/lít.

C. $20 481$ VNĐ/lít.

D. $20 000$ VNĐ/lít.

Hướng dẫn giải:

Ta có:

Giá xăng năm 2017: $16000(1 + 0,025).$

Giá xăng năm 2018: $16000{(1 + 0,025)^2}.$

… …

Giá xăng năm 2025: $160000{(1 + 0,025)^9}$ $= 19981$ VNĐ/lít.

> **Đáp án: B**