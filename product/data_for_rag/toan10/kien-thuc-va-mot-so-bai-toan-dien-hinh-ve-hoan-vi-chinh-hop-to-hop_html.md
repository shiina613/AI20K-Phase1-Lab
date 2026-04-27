# Kiến thức và một số bài toán điển hình về hoán vị - chỉnh hợp - tổ hợp

<!-- chunk:0 level:0 source:https://toanmath.com/2018/11/kien-thuc-va-mot-so-bai-toan-dien-hinh-ve-hoan-vi-chinh-hop-to-hop.html -->
Bài viết trình bày các lý thuyết cơ bản, các công thức tính hoán vị – chỉnh hợp – tổ hợp, cách phân biệt để tránh nhầm lẫn giữa các khái niệm này, đồng thời đưa ra một số bài toán điển hình và hướng dẫn phương pháp giải toán để bạn đọc nắm chắc bài toán hoán vị – chỉnh hợp – tổ hợp.

<!-- chunk:1 level:1 source:https://toanmath.com/2018/11/kien-thuc-va-mot-so-bai-toan-dien-hinh-ve-hoan-vi-chinh-hop-to-hop.html -->
## I. HOÁN VỊ

1. Giai thừa

$n! = 1.2.3 \ldots n.$

$n! = (n – 1)!n.$

$\frac{{n!}}{{p!}} = (p + 1)(p + 2) \ldots n$ (với $n > p$).

$\frac{{n!}}{{(n – p)!}} = (n – p + 1)(n – p + 2) \ldots n$ (với $n > p$).

Quy ước: $0! = 1.$

2. Hoán vị (không lặp)

Một tập hợp gồm $n$ phần tử ($n ≥ 1$). Mỗi cách sắp xếp $n$ phần tử này theo một thứ tự nào đó được gọi là một hoán vị của $n$ phần tử.

Số các hoán vị của $n$ phần tử là: ${P_n} = n!.$

3. Hoán vị lặp

Cho $k$ phần tử khác nhau: ${a_1},{a_2}, \ldots ,{a_k}$. Một cách sắp xếp $n$ phần tử trong đó gồm $n_1$ phần tử $a_1$, $n_2$ phần tử $a_2$, …, $n_k$ phần tử $a_k$ $\left( {{n_1} + {n_2} + \ldots + nk = n} \right)$ theo một thứ tự nào đó được gọi là một hoán vị lặp cấp $n$ và kiểu $\left( {{n_1},{n_2}, \ldots ,{n_k}} \right)$ của $k$ phần tử.

Số các hoán vị lặp cấp $n$ kiểu $\left( {{n_1},{n_2}, \ldots ,{n_k}} \right)$ của $k$ phần tử là: ${P_n}\left( {{n_1},{n_2}, \ldots ,{n_k}} \right) = \frac{{n!}}{{{n_1}!{n_2}! \ldots {n_k}!}}.$

4. Hoán vị vòng quanh

Cho tập $A$ gồm $n$ phần tử. Một cách sắp xếp $n$ phần tử của tập $A$ thành một dãy kín được gọi là một hoán vị vòng quanh của $n$ phần tử.

Số các hoán vị vòng quanh của $n$ phần tử là: ${Q_n} = (n – 1)!.$

<!-- chunk:2 level:1 source:https://toanmath.com/2018/11/kien-thuc-va-mot-so-bai-toan-dien-hinh-ve-hoan-vi-chinh-hop-to-hop.html -->
## II. CHỈNH HỢP

1. Chỉnh hợp (không lặp)

Cho tập hợp $A$ gồm $n$ phần tử. Mỗi cách sắp xếp $k$ phần tử của $A$ $(1 \le k \le n)$ theo một thứ tự nào đó được gọi là một chỉnh hợp chập $k$ của $n$ phần tử của tập $A.$

Số chỉnh hợp chập $k$ của $n$ phần tử: $A_n^k = n(n – 1)(n – 2) \ldots (n – k + 1)$ $= \frac{{n!}}{{(n – k)!}}.$

+ Công thức trên cũng đúng cho trường hợp $k = 0$ hoặc $k = n.$

+ Khi $k = n$ thì $A_n^n = {P_n} = n!.$

2. Chỉnh hợp lặp

Cho tập $A$ gồm $n$ phần tử. Một dãy gồm $k$ phần tử của $A$, trong đó mỗi phần tử có thể được lặp lại nhiều lần, được sắp xếp theo một thứ tự nhất định được gọi là một chỉnh hợp lặp chập $k$ của $n$ phần tử của tập $A.$

Số chỉnh hợp lặp chập $k$ của $n$ phần tử: $\overline {A_n^k} = {n^k}.$

<!-- chunk:3 level:1 source:https://toanmath.com/2018/11/kien-thuc-va-mot-so-bai-toan-dien-hinh-ve-hoan-vi-chinh-hop-to-hop.html -->
## III. TỔ HỢP

1. Tổ hợp (không lặp)

Cho tập $A$ gồm $n$ phần tử. Mỗi tập con gồm $k$ $(1 \le k \le n)$ phần tử của $A$ được gọi là một tổ hợp chập $k$ của $n$ phần tử.

Số các tổ hợp chập $k$ của $n$ phần tử: $C_n^k = \frac{{A_n^k}}{{k!}} = \frac{{n!}}{{k!(n – k)!}}.$

Qui ước: $C_n^0 = 1.$

Tính chất: $C_n^0 = C_n^n = 1$, $C_n^k = C_n^{n – k}$, $C_n^k = C_{n – 1}^{k – 1} + C_{n – 1}^k$, $C_n^k = \frac{{n – k + 1}}{k}C_n^{k – 1}.$

2. Tổ hợp lặp

Cho tập $A = \left\{ {{a_1};{a_2}; \ldots ;{a_n}} \right\}$ và số tự nhiên $k$ bất kì. Một tổ hợp lặp chập $k$ của $n$ phần tử là một tập hợp gồm $k$ phần tử, trong đó mỗi phần tử là một trong $n$ phần tử của $A.$

Số tổ hợp lặp chập $k$ của $n$ phần tử: $\overline {C_n^k} = C_{n + k – 1}^k = C_{n + k – 1}^{n – 1}.$

3. Phân biệt chỉnh hợp và tổ hợp

Chỉnh hợp và tổ hợp liên hệ nhau bởi công thức: $A_n^k = k!C_n^k.$

Chỉnh hợp: Có thứ tự.

Tổ hợp: Không có thứ tự.

Suy ra: Những bài toán mà kết quả phụ thuộc vào vị trí các phần tử $→$ chỉnh hợp. Ngược lại là tổ hợp.

Cách lấy $k$ phần tử từ tập $n$ phần tử $(k \le n)$:

+ Không thứ tự, không hoàn lại: $C_n^k.$

+ Có thứ tự, không hoàn lại: $A_n^k.$

+ Có thứ tự, có hoàn lại: $\overline {A_n^k} .$

<!-- chunk:4 level:2 source:https://toanmath.com/2018/11/kien-thuc-va-mot-so-bai-toan-dien-hinh-ve-hoan-vi-chinh-hop-to-hop.html -->
## Bài toán 1: Có bao nhiêu cách xếp $7$ học sinh $A$, $B$, $C$, $D$, $E$, $F$, $G$ vào một hàng ghế dài gồm $7$ ghế sao cho hai bạn $B$ và $F$ ngồi ở hai ghế đầu?

A. $720$ cách.

B. $5040$ cách.

C. $240$ cách.

D. $120$ cách.

Chọn C.

Ta thấy ở đây bài toán xuất hiện hai đối tượng.

Đối tượng 1: Hai bạn $B$ và $F$ (hai đối tượng này có tính chất riêng).

Đối tượng 2: Các bạn còn lại có thể thay đổi vị trí cho nhau.

Bước 1: Ta sử dụng tính chất riêng của hai bạn $B$ và $F$ trước. Hai bạn này chỉ ngồi đầu và ngồi cuối, hoán đổi cho nhau nên có $2!$ cách xếp.

Bước 2: Xếp vị trí cho các bạn còn lại, ta có $5!$ cách xếp.

Vậy ta có $2!.5! = 240$ cách xếp.

Nhận xét: Để nhận dạng một bài toán đếm có sử dụng hoán vị của $n$ phần tử, ta dựa trên dấu hiệu:

a. Tất cả $n$ phần tử đều có mặt.

b. Mỗi phần tử chỉ xuất hiện $1$ lần.

c. Có sự phân biệt thứ tự giữa các phần tử.

d. Số cách xếp $n$ phần tử là số hoán vị của $n$ phần tử đó ${P_n} = n!.$

<!-- chunk:5 level:2 source:https://toanmath.com/2018/11/kien-thuc-va-mot-so-bai-toan-dien-hinh-ve-hoan-vi-chinh-hop-to-hop.html -->
## Bài toán 2: Một nhóm $9$ người gồm ba đàn ông, bốn phụ nữ và hai đứa trẻ đi xem phim. Hỏi có bao nhiêu cách xếp họ ngồi trên một hàng ghế sao cho mỗi đứa trẻ ngồi giữa hai phụ nữ và không có hai người đàn ông nào ngồi cạnh nhau?

A. $288.$

B. $864.$

C. $24.$

D. $576.$

Chọn B.

Kí hiệu $T$ là ghế đàn ông ngồi, $N$ là ghế cho phụ nữ ngồi, $C$ là ghế cho trẻ con ngồi. Ta có các phương án sau:

Phương án 1: $TNCNTNCNT.$

Phương án 2: $TNTNCNCNT.$

Phương án 3: $TNCNCNTNT.$

Xét phương án 1: Ba vị trí ghế cho đàn ông có $3!$ cách.

Bốn vị trí ghế cho phụ nữ có thể có $4!$ cách.

Hai vị trí ghế trẻ con ngồi có thể có $2!$ cách.

Theo quy tắc nhân thì ta có $3!.4!.2! = 288$ cách.

Lập luận tương tự cho phương án 2 và phương án 3.

Theo quy tắc cộng thì ta có $288 + 288 + 288 = 864$ cách.

Nhận xét: Với các bài toán gồm có ít phần tử và vừa cần chia trường hợp vừa thực hiện theo bước thì ta cần chia rõ trường hợp trước, lần lượt thực hiện từng trường hợp (sử dụng quy tắc nhân từng bước) sau đó mới áp dụng quy tắc cộng để cộng số cách trong các trường hợp với nhau.

<!-- chunk:6 level:2 source:https://toanmath.com/2018/11/kien-thuc-va-mot-so-bai-toan-dien-hinh-ve-hoan-vi-chinh-hop-to-hop.html -->
## Bài toán 3: Một chồng sách gồm $4$ quyển sách Toán, $3$ quyển sách Vật lý, $5$ quyển sách Hóa học. Hỏi có bao nhiêu cách xếp các quyển sách trên thành một hàng ngang sao cho $4$ quyển sách Toán đứng cạnh nhau, $3$ quyển Vật lý đứng cạnh nhau?

A. $1$ cách.

B. $5040$ cách.

C. $725760$ cách.

D. $144$ cách.

Chọn C.

Bước 1: Do đề bài cho $4$ quyển sách Toán đứng cạnh nhau nên ta sẽ coi như “buộc” các quyển sách Toán lại với nhau thì số cách xếp cho “buộc” Toán này là $4!$ cách.

Bước 2: Tương tự ta cũng “buộc” $3$ quyển sách Lý lại với nhau, thì số cách xếp cho “buộc” Lý này là $3!$ cách.

Bước 3: Lúc này ta sẽ đi xếp vị trí cho $7$ phần tử trong đó có:

+ $1$ “buộc” Toán.

+ $1$ “buộc” Lý.

+ $5$ quyển Hóa.

Thì sẽ có $7!$ cách xếp.

Vậy theo quy tắc nhân ta có $7!.4!.3! = 725760$ cách xếp.

Nhận xét: Với các dạng bài tập yêu cầu xếp hai hoặc nhiều phần tử đứng cạnh nhau thì ta sẽ “buộc” các phần tử này một nhóm và coi như $1$ phần tử.

<!-- chunk:7 level:2 source:https://toanmath.com/2018/11/kien-thuc-va-mot-so-bai-toan-dien-hinh-ve-hoan-vi-chinh-hop-to-hop.html -->
## Bài toán 4: Một câu lạc bộ phụ nữ của phường Khương Mai (Thanh Xuân, Hà Nội) có $39$ hội viên. Phường Khương Mai có tổ chức một hội thảo cần chọn ra $9$ người xếp vào $9$ vị trí lễ tân khác nhau ở cổng chào, $12$ người vào $12$ vị trí khác nhau ở ghế khách mới. Hỏi có bao nhiêu cách chọn các hội viên để đi tham gia các vị trí trong hội thao theo quy định?

A. $A_{39}^9.A_{39}^{12}$.

B. $C_{39}^9.C_{30}^{12}$.

C. $C_{39}^9.C_{39}^{12}$.

D. $A_{39}^9.A_{30}^{12}$.

Phân tích: Bài toán sử dụng quy tắc nhân khi ta phải thực hiện hai bước:

Bước 1: Chọn $9$ người vào vị trí lễ tân.

Bước 2: Chọn $12$ người vào vị trí khách mời.

Dấu hiệu nhận biết sử dụng chỉnh hợp ở phần nhận xét.

Chọn D.

Bước 1: Chọn người vào vị trí lễ tân. Do ở đây được sắp theo thứ tự nên ta sẽ sử dụng chỉnh hợp. Số cách chọn ra $9$ người vào vị trí lễ tân là $A_{39}^9$ cách.

Bước 2: Chọn người vào vị trí khách mời. Số cách chọn là $12$ thành viên trong số các thành viên còn lại để xếp vào khách mời là $A_{30}^{12}$ cách.

Vậy theo quy tắc nhân thì số cách chọn các hội viên để đi dự hội thảo theo đúng quy định là: $A_{39}^9 \cdot A_{30}^{12}$ cách.

Nhận xét: Để nhận dạng một bài toán đếm có sử dụng chỉnh hợp chập $k$ của $n$ phần tử, ta cần có các dấu hiệu:

a. Phải chọn $k$ phần tử từ $n$ phần tử cho trước.

b. Có sự phân biệt thứ tự giữa $k$ phần tử được chọn.

c. Số cách chọn $k$ phần tử có phân biệt thứ tự từ $n$ phần tử là $A_n^k$ cách.

<!-- chunk:8 level:2 source:https://toanmath.com/2018/11/kien-thuc-va-mot-so-bai-toan-dien-hinh-ve-hoan-vi-chinh-hop-to-hop.html -->
## Bài toán 5: Có $6$ học sinh và $2$ thầy giáo được xếp thành hàng ngang. Hỏi có bao nhiêu cách xếp sao cho hai thầy giáo không đứng cạnh nhau?

A. $30240$ cách.

B. $720$ cách.

C. $362880$ cách.

D. $1440$ cách.

Chọn A.

Cách 1: Trước hết, xếp $6$ học sinh thành một hàng có $6!$ cách.

Lúc này giữa hai học sinh bất kì sẽ tạo nên một vách ngăn và $6$ học sinh sẽ tạo nên $7$ vị trí có thể xếp các thầy vào đó tính cả hai vị trí ở hai đầu hàng (hình minh họa bên dưới). $7$ vị trí dấu nhân chính là $7$ vách ngăn được tạo ra.

<img link="data_for_rag/toan10/images/kien-thuc-va-mot-so-bai-toan-dien-hinh-ve-hoan-vi-chinh-hop-to-hop-1.png" alt="kien-thuc-va-mot-so-bai-toan-dien-hinh-ve-hoan-vi-chinh-hop-to-hop-1">

Do đề yêu cầu $2$ thầy giáo không đứng cạnh nhau nên ta xếp $2$ thầy giáo vào $2$ trong $7$ vị trí vách ngăn được tạo ra có $A_7^2$ cách.

Theo quy tắc nhân ta có tất cả $6!A_7^2 = 30240$ cách xếp.

Cách 2:

Có $8!$ cách xếp $8$ người.

Buộc hai giáo viên lại với nhau thì có $2!$ cách buộc.

Khi đó có $2.7!$ cách xếp. Mà hai giáo viên không đứng cạnh nhau nên số cách xếp là $8! – 2.7! = 30140$ cách xếp.

Nhận xét: Khi bài toán yêu cầu xếp hai hoặc nhiều phần tử không đứng cạnh nhau. Chúng ta có thể tạo ra các “vách ngăn” các phần tử này trước khi xếp chúng.

<!-- chunk:9 level:2 source:https://toanmath.com/2018/11/kien-thuc-va-mot-so-bai-toan-dien-hinh-ve-hoan-vi-chinh-hop-to-hop.html -->
## Bài toán 6: Từ $5$ bông hồng vàng, $3$ bông hồng trắng và $4$ bông hồng đỏ (các bông hoa xem như đôi một khác nhau), người ta muốn chọn một bó hồng gồm $7$ bông, hỏi có bao nhiêu cách chọn bó hoa trong đó có ít nhất $3$ bông hồng vàng và $3$ bông hồng đỏ?

A. $10$ cách.

B. $20$ cách.

C. $120$ cách.

D. $150$ cách.

Phân tích: Ta thấy do chỉ chọn $7$ bông hồng mà có ít nhất $3$ bông hồng vàng và ít nhất $3$ bông hồng đỏ nên chỉ có $3$ trường hợp sau:

Trường hợp 1: Chọn được $3$ bông hồng vàng và $4$ bông hồng đỏ.

Trường hợp 2: Chọn được $4$ bông hồng vàng và $3$ bông hồng đỏ.

Trường hợp 3: Chọn được $3$ bông hồng vàng, $3$ bông hồng đỏ và $1$ bông hồng trắng.

Chọn D.

Trường hợp 1:

Số cách chọn $3$ bông hồng vàng là $C_5^3$ cách.

Số cách chọn $4$ bông hồng đỏ là $C_4^4$ cách.

Theo quy tắc nhân thì có $C_5^3.C_4^4 = 10$ cách.

Trường hợp 2: Tương tự trường hợp 1 thì ta có $C_5^4.C_4^3 = 20$ cách.

Trường hợp 3: Tương tự thì có $C_5^3.C_4^3.C_3^1 = 120$ cách.

Vậy theo quy tắc cộng thì có $10 + 20 + 120 = 150$ cách.

Nhận xét:

Để nhận dạng bài toán sử dụng tổ hợp chập $k$ của $n$ phần tử, ta dựa trên dấu hiệu:

a. Phải chọn ra $k$ phần tử từ $n$ phần tử cho trước.

b. Không phân biệt thứ tự giữa $k$ phần tử được chọn.

c. Số cách chọn $k$ phần tử không phân biệt thứ tự từ $n$ phần tử đã cho là $C_n^k$ cách.

<!-- chunk:10 level:2 source:https://toanmath.com/2018/11/kien-thuc-va-mot-so-bai-toan-dien-hinh-ve-hoan-vi-chinh-hop-to-hop.html -->
## Bài toán 7: Đội thanh niên xung kích của một trường phổ thông có $12$ học sinh, gồm $5$ học sinh lớp A, $4$ học sinh lớp B và $3$ học sinh lớp C. Cần chọn $4$ học sinh đi làm nhiệm vụ sao cho $4$ học sinh này thuộc không quá $2$ trong $3$ lớp trên. Hỏi có bao nhiêu cách chọn như vậy?

A. $120.$

B. $90.$

C. $270.$

D. $255.$

Chọn D.

Số cách chọn $4$ học sinh bất kì từ $12$ học sinh là $C_{12}^4 = 495$ cách.

Số cách chọn $4$ học sinh mà mỗi lớp có ít nhất một em được tính như sau:

Trường hợp 1: Lớp A có hai học sinh, các lớp B, C mỗi lớp có $1$ học sinh:

Chọn $2$ học sinh trong $5$ học sinh lớp A có $C_5^2$ cách.

Chọn $1$ học sinh trong $4$ học sinh lớp B có $C_4^1$ cách.

Chọn $1$ học sinh trong $3$ học sinh lớp C có $C_3^1$ cách.

Suy ra số cách chọn là $C_5^2.C_4^1.C_3^1 = 120$ cách.

Trường hợp 2: Lớp B có $2$ học sinh, các lớp A, C mỗi lớp có $1$ học sinh:

Tương tự ta có số cách chọn là $C_5^1.C_4^2.C_3^1 = 90$ cách.

Trường hợp 3: Lớp C có $2$ học sinh, các lớp A, B mỗi lớp có $1$ học sinh:

Tương tự ta có số cách chọn là $C_5^1.C_4^1.C_3^2 = 60$ cách.

Vậy số cách chọn $4$ học sinh mà mỗi lớp có ít nhất một học sinh là $120 + 90 + 60 = 270$ cách.

Số cách chọn ra $4$ học sinh thuộc không quá $2$ trong $3$ lớp trên là $495 – 270 = 225$ cách.

Nhận xét:

Trong nhiều bài toán, làm trực tiếp sẽ khó trong việc xác định các trường hợp hoặc các bước thì ta nên làm theo hướng gián tiếp như bài toán ở ví dụ 9.

Ta sử dụng cách làm gián tiếp khi bài toán giải bằng cách trực tiếp gặp khó khăn do xảy ra quá nhiều trường hợp, chúng ta tìm cách gián tiếp bằng cách xét bài toán đối.

<!-- chunk:11 level:2 source:https://toanmath.com/2018/11/kien-thuc-va-mot-so-bai-toan-dien-hinh-ve-hoan-vi-chinh-hop-to-hop.html -->
## Bài toán 8: Với các chữ số $0,1,2,3,4,5$ có thể lập được bao nhiêu số gồm $8$ chữ số, trong đó chữ số $1$ có mặt $3$ lần, mỗi chữ số khác có mặt đúng một lần?

A. $6720$ số.

B. $40320$ số.

C. $5880$ số.

D. $840$ số.

Chọn C.

Giả sử các số tự nhiên gồm $8$ chữ số tương ứng với $8$ ô.

<img link="data_for_rag/toan10/images/kien-thuc-va-mot-so-bai-toan-dien-hinh-ve-hoan-vi-chinh-hop-to-hop-2.png" alt="">

Do chữ số $1$ có mặt $3$ lần nên ta sẽ coi như tìm số các số thỏa mãn đề bài được tạo nên từ $8$ số $0,1,1,1,2,3,4,5.$

Số hoán vị của $8$ số $0,1,1,1,2,3,4,5$ trong $8$ ô trên là $8!.$

Mặt khác chữ số $1$ lặp lại $3$ lần nên số cách xếp là $\frac{{8!}}{{3!}}$ kể cả trường hợp số $0$ đứng đầu.

Xét trường hợp ô thứ nhất là chữ số $0$, thì số cách xếp là $\frac{{7!}}{{3!}}.$

<!-- chunk:12 level:2 source:https://toanmath.com/2018/11/kien-thuc-va-mot-so-bai-toan-dien-hinh-ve-hoan-vi-chinh-hop-to-hop.html -->
## Bài toán 9: Cho $8$ bạn học sinh $A,B,C,D,E,F,G,H$. Hỏi có bao nhiêu cách xếp $8$ bạn đó ngồi xung quanh $1$ bàn tròn có $8$ ghế?

A. $40320$ cách.

B. $5040$ cách.

C. $720$ cách.

D. $40319$ cách.

Chọn B.

Ta thấy ở đây xếp các vị trí theo hình tròn nên ta phải cố định vị trí một bạn.

Ta chọn cố định vị trị của $A$, sau đó xếp vị trí cho $7$ bạn còn lại có $7!$ cách.

Vậy có $7! = 5040$ cách.

<!-- chunk:13 level:2 source:https://toanmath.com/2018/11/kien-thuc-va-mot-so-bai-toan-dien-hinh-ve-hoan-vi-chinh-hop-to-hop.html -->
## Bài toán 10: Một thầy giáo có $10$ cuốn sách khác nhau trong đó có $4$ cuốn sách Toán, $3$ cuốn sách Lí, $3$ cuốn sách Hóa. Thầy muốn lấy ra $5$ cuốn và tặng cho $5$ em học sinh $A,B,C,D,E$ mỗi em một cuốn. Hỏi thầy giáo có bao nhiêu cách tặng cho các em học sinh sao cho sau khi tặng xong, mỗi một trong ba loại sách trên đều còn ít nhất một cuốn.

A. $204$ cách.

B. $24480$ cách.

C. $720$ cách.

D. $2520$ cách.

Chọn B.

Ta thấy với bài toán này nếu làm trực tiếp thì sẽ khá khó, nên ta sẽ làm theo cách gián tiếp. Tìm bài toán đối đó là tìm số cách sao cho sau khi tặng sách xong có một môn hết sách.

Trường hợp 1: Môn Toán hết sách:

Số cách chọn $4$ cuốn sách Toán là $1$ cách.

Số cách chọn $1$ cuốn trong $6$ cuốn còn lại là $6$ cách.

Vậy có $6$ cách chọn sách.

Số cách tặng $5$ cuốn sách đó cho $5$ em học sinh là $A_5^5 = 120$ cách.

Vậy có $6.120 = 720$ cách.

Trường hợp 2: Môn Lí hết sách:

Số cách chọn $3$ cuốn sách Lí là $1$ cách.

Số cách chọn $2$ cuốn trong $7$ cuốn còn lại là $C_7^2$ cách.

Vậy có $21$ cách chọn sách.

Số cách tặng $5$ cuốn sách đó cho $5$ em học sinh là $A_5^5 = 120$ cách.

Vậy có $21.120 = 2520$ cách.

Trường hợp 3: Môn Hóa hết sách: Tương tự trường hợp 2 thì có $2520$ cách.

Số cách chọn $5$ cuốn bất kì trong $10$ cuốn và tặng cho $5$ em là $C_{10}^5.A_5^5 = 30240$ cách.

Vậy số cách chọn sao cho sau khi tặng xong, mỗi loại sách trên đều còn lại ít nhất một cuốn là $30240 – 720 – 2520 – 2520 = 24480$ cách.

Nhận xét: Ở đây có nhiều độc giả không xét đến công đoạn sau khi chọn sách còn công đoạn tặng sách nữa. Do các bạn $A,B,C,D,E$ là khác nhau nên mỗi cách tặng sách các môn cho các bạn là khác nhau, nên ta phải xét thêm công đoạn đó.