# Phương pháp giải bài toán đếm

<!-- chunk:0 level:0 source:https://toanmath.com/2018/06/phuong-phap-giai-bai-toan-dem.html -->
Bài viết hướng dẫn phương pháp giải bài toán đếm trong chủ đề hoán vị – chỉnh hợp – tổ hợp, bao gồm bài toán đếm số, bài toán xếp đồ vật, bài toán phân chia công việc, bài toán đếm liên quan đến hình học.

**Phương pháp**: Dựa vào quy tắc cộng, quy tắc nhân và các khái niệm hoán vị, chỉnh hợp, tổ hợp.

Một số dấu hiệu giúp chúng ta nhận biết được hoán vị, chỉnh hợp hay tổ hợp.

1. Hoán vị: Các dấu hiệu đặc trưng để giúp ta nhận dạng một hoán vị của $n$ phần tử là:

• Tất cả $n$ phần tử đều phải có mặt.

• Mỗi phần tử xuất hiện một lần.

• Có thứ tự giữa các phần tử.

2. Chỉnh hợp: Ta sẽ sử dụng khái niệm chỉnh hợp khi:

• Cần chọn $k$ phần tử từ $n$ phần tử, mỗi phần tử xuất hiện một lần.

• $k$ phần tử đã cho được sắp xếp thứ tự.

3. Tổ hợp: Ta sử dụng khái niệm tổ hợp khi:

• Cần chọn $k$ phần tử từ $n$ phần tử, mỗi phần tử xuất hiện một lần.

• Không quan tâm đến thứ tự $k$ phần tử đã chọn.

Các dạng toán thường gặp và ví dụ minh họa

<!-- chunk:1 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-bai-toan-dem.html -->
## Ví dụ 1. Từ các chữ số $0, 1, 2, 3, 4, 5, 6$ có thể lập được bao nhiêu số chẵn, mỗi số có $5$ chữ số khác nhau trong đó có đúng hai chữ số lẻ và $2$ chữ số lẻ đứng cạnh nhau?

Gọi$A$ là số tự nhiên có hai chữ số lẻ khác nhau lấy từ các số $0, 1, 2, 3, 4, 5, 6.$

Số cách chọn được $A$ là $A_{3}^{2}=6$.

Số chẵn có $5$ chữ số khác nhau, trong đó có đúng hai chữ số lẻ và $2$ chữ số lẻ đứng cạnh nhau phải chứa $A$ và ba trong $4$ chữ số $0, 2, 4, 6.$

Gọi $\overline{abcd}$ $(a, b, c, d \in \{ A,0,2,4,6\})$ là số thỏa mãn yêu cầu bài toán.

• Trường hợp 1: Nếu $a=A$ thì có $1$ cách chọn $a$ và $A_{4}^{3}$ cách chọn $b, c, d$.

• Trường hợp 2: Nếu $a \ne A$ thi có $3$ cách chọn $a.$

+ Nếu $b=A$ có $1$ cách chọn $b$ và $A_{3}^{2}$ cách chọn $c,d$.

+ Nếu $c=A$ có $1$ cách chọn $c$ và $A_{3}^{2}$ cách chọn $b,d$.

Vậy có $A_{3}^{2}\left( A_{4}^{3}+3\left( 1.A_{3}^{2}+1.A_{3}^{2} \right) \right)=360$ số thỏa mãn yêu cầu bài toán.

<!-- chunk:2 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-bai-toan-dem.html -->
## Ví dụ 2. Từ các số $1, 2, 3, 4, 5, 6$ lập được bao nhiêu số tự nhiên:

1. Gồm $4$ chữ số.

2. Gồm $3$ chữ số đôi một khác nhau.

3. Gồm $4$ chữ số đôi một khác nhau và là chữ số tự nhiên chẵn.

4. Gồm $4$ chữ số đôi một khác nhau và không bắt đầu bằng chữ số $1$.

5. Gồm $6$ chữ số đôi một khác nhau và hai chữ số $1$ và $2$ không đứng cạnh nhau.

1. Gọi số cần lập là: $x = \overline {abcd} .$ Ta có: $a$ có $6$ cách chọn, $b$ có $6$ cách chọn, $c$ có $6$ cách chọn, $d$ có $6$ cách chọn. Vậy có ${6^4} = 1296$ số.

2. Mỗi số cần lập ứng với một chỉnh hợp chập $3$ của $6$ phần tử $1, 2, 3, 4, 5, 6.$ Nên số các số cần lập là $A_6^3 = 120$ số.

3. Gọi số cần lập là: $x = \overline {abcd} .$ Vì $x$ chẵn nên có $3$ cách chọn $d$. Ứng với mỗi cách chọn $d$ sẽ có $A_{5}^{3}$ cách chọn $a, b, c$. Vậy có $3.A_{5}^{3}=180$ số.

4. Gọi số cần lập là: $x=\overline{abcd}.$ Vì $a\ne 1$ nên $a$ có $5$ cách chọn. Ứng với mỗi cách chọn $a$ ta có $A_{5}^{3}$ cách chọn $b, c, d$. Vậy có $5.A_{5}^{3}=300$ số.

5. Gọi $x$ là số có $6$ chữ số đôi một khác nhau và hai chữ số $1$ và $2$ luôn đứng cạnh nhau.

Đặt $y=12$ khi đó $x$ có dạng $\overline{abcde}$ với $a,b,c,d,e$ đôi một khác nhau và thuộc tập $\left\{ y,3,4,5,6 \right\}$ nên có ${{P}_{5}}=5!=120$ số.

Khi hoán vị hai số $1, 2$ ta được một số khác nên có $120.2=240$ số $x.$

Vậy số thỏa yêu cầu bài toán là: ${{P}_{6}}-240=480$ số.

<!-- chunk:3 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-bai-toan-dem.html -->
## Ví dụ 3. Có bao nhiêu số tự nhiên gồm $7$ chữ số, biết rằng chữ số $2$ có mặt hai lần, chữ số $3$ có mặt ba lần và các chữ số còn lại có mặt nhiều nhất một lần?

Ta đếm các số có $7$ chữ số được chọn từ các số $\left\{ 2, 2, 3, 3, 3, a, b \right\}$ với $a, b \in \left\{0, 1, 4, 5, 6, 7, 8, 9 \right\}$, kể cả số $0$ đứng đầu.

Ta có được $7!$ số như vậy. Tuy nhiên khi hoán vị hai số $2$ cho nhau hoặc các số $3$ cho nhau thì ta được số không đổi do đó có tất cả $\frac{7!}{2!.3!}=420$ số.

Vì có $A_{8}^{2}$ cách chọn $a,b$ nên ta có: $480.A_{8}^{2}=26880$ số.

Ta đếm các số có $6$ chữ số được chọn từ các số $\left\{ 2,2,3,3,3,x \right\}$ với $x\in \left\{ 1,4,5,6,7,8,9 \right\}$.

Tương tự như trên ta tìm được $\frac{6!}{2!.3!}A_{7}^{1}=420$ số.

Vậy số các số thỏa yêu cầu bài toán: $26880 – 420 = 26460$.

<!-- chunk:4 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-bai-toan-dem.html -->
## Ví dụ 4. Hỏi có thể lập được bao nhiêu số tự nhiên có $4$ chữ số sao cho trong mỗi số đó, chữ số hàng ngàn lớn hơn hàng trăm, chữ số hàng trăm lớn hơn hàng chục và chữ số hàng chục lớn hơn hàng đơn vị.

Gọi $x = \overline {{a_1}{a_2}{a_3}{a_4}}$ với $9 \ge {a_1} > {a_2} > {a_3} > {a_4} \ge 0$ là số cần lập.

$X = \left\{ {0;{\rm{ }}1;{\rm{ }}2;{\rm{ }}…;{\rm{ }}8;{\rm{ }}9} \right\}.$

Từ $10$ phần tử của $X$ ta chọn ra $4$ phần tử bất kỳ thì chỉ lập được $1$ số $A$, nghĩa là một tổ hợp chập $4$ của $10.$

Vậy có $C_{10}^4 = 210$ số.

<!-- chunk:5 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-bai-toan-dem.html -->
## Ví dụ 5. Từ các số $1,2,3,4,5,6,7,8,9$ có thể lập được bao nhiêu số tự nhiên có $6$ chữ số khác nhau và tổng các chữ số ở hàng chục, hàng trăm, hàng ngàn bằng $8.$

Gọi $n = \overline {{a_1}{a_2}{a_3}{a_4}{a_5}{a_6}}$ là một số thỏa yêu cầu bài toán thì ${a_3} + {a_4} + {a_5} = 8.$

Có hai bộ $3$ số có tổng bằng $8$ trong các số $1,2,3,4,5,6,7,8,9$ là: $\left\{ {1;2;5} \right\}$ và $\left\{ {1;3;4} \right\}.$

Nếu ${a_3};{a_4};{a_5} \in \left\{ {1;2;5} \right\}$ thì ${a_3},{a_4},{a_5}$ có $3!$ cách chọn và ${a_1},{a_2},{a_6}$ có $A_6^3$ cách chọn suy ra có $3!A_6^3 = 720$ số thỏa yêu cầu.

Nếu ${a_3};{a_4};{a_5} \in \left\{ {1;2;5} \right\}$ thì cũng có $720$ số thỏa yêu cầu.

Vậy có $720 + 720 = 1400$ số thỏa yêu cầu.

<!-- chunk:6 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-bai-toan-dem.html -->
## Ví dụ 6. Đội tuyển học sinh giỏi của một trường gồm $18$ em, trong đó có $7$ học sinh khối 12, $6$ học sinh khối 11 và $5$ học sinh khối 10. Hỏi có bao nhiêu cách cử $8$ học sinh đi dự đại hội sao cho mỗi khối có ít nhất $1$ học sinh được chọn.

Vì có $7$ học sinh khối 12, $6$ học sinh khối 11 và $5$ học sinh khối 10 nên khi chọn $8$ học sinh bất kỳ, thì sẽ luôn có học sinh của hai khối hoặc cả ba khối.

Số cách chọn $8$ học sinh chỉ gồm học sinh khối 12 và khối 11 là: $C_{13}^8$.

Số cách chọn $8$ học sinh chỉ gồm học sinh khối 11 và khối 10 là: $C_{11}^8$.

Số cách chọn $8$ học sinh chỉ gồm học sinh khối 12 và khối 10 là: $C_{12}^8$.

Suy ra số cách chọn $8$ học sinh gồm hai khối là: $C_{13}^8 + C_{11}^8 + C_{12}^8 = 1947.$

Số cách chọn thỏa mãn yêu cầu bài toán: $C_{18}^8 – 1947 = 41811.$

<!-- chunk:7 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-bai-toan-dem.html -->
## Ví dụ 7. Một cuộc họp có $13$ người, lúc ra về mỗi người đều bắt tay người khác một lần, riêng chủ tọa chỉ bắt tay ba người. Hỏi có bao nhiêu cái bắt tay?

Số cái bắt tay của $12$ người (trừ chủ tọa) là: $C_{12}^2$.

Vậy có $C_{12}^2 + 3 = 69$ cái bắt tay.

[ads]

<!-- chunk:8 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-bai-toan-dem.html -->
## Ví dụ 8. Trong một môn học, thầy giáo có $30$ câu hỏi khác nhau gồm $5$ câu khó, $10$ câu trung bình và $15$ câu dễ. Từ $30$ câu hỏi đó có thể lập được bao nhiêu đề kiểm tra, mỗi đề gồm $5$ câu hỏi khác nhau, sao cho trong mỗi đề nhất thiết phải có đủ cả $3$ câu (khó, dễ, trung bình) và số câu dễ không ít hơn $2$?

Ta có các trường hợp sau:

+ Trường hợp 1: Đề thi gồm $2$ câu dễ, $2$ câu trung bình, $1$ câu khó: $C_{15}^2.C_{10}^2.C_5^1$.

+ Trường hợp 2: Đề thi gồm $2$ câu dễ, $1$ câu trung bình, $2$ câu khó: $C_{15}^2.C_{10}^1.C_5^2$.

+ Trường hợp 3: Đề thi gồm $3$ câu dễ, $1$ câu trung bình, $1$ câu khó: $C_{15}^3.C_{10}^1.C_5^1$.

Vậy có: $56875$ đề kiểm tra.

<!-- chunk:9 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-bai-toan-dem.html -->
## Ví dụ 9. Hai nhóm người cần mua nền nhà, nhóm thứ nhất có $2$ người và họ muốn mua $2$ nền kề nhau, nhóm thứ hai có $3$ người và họ muốn mua $3$ nền kề nhau. Họ tìm được một lô đất chia thành $7$ nền đang rao bán (các nền như nhau và chưa có người mua). Tính số cách chọn nền của mỗi người thỏa yêu cầu trên.

Xem lô đất có $4$ vị trí gồm $2$ vị trí $1$ nền, $1$ vị trí $2$ nền và $1$ vị trí $3$ nền.

Nhóm thứ nhất chọn $1$ vị trí cho $2$ nền có $4$ cách và mỗi cách có $2!=2$ cách chọn nền cho mỗi người. Suy ra có $4.2=8$ cách chọn nền.

Nhóm thứ hai chọn $1$ trong $3$ vị trí còn lại cho $3$ nền có $3$ cách và mỗi cách có $3!=6$ cách chọn nền cho mỗi người.

Suy ra có $3.6=18$ cách chọn nền.

Vậy có $8.18=144$ cách chọn nền cho mỗi người.

<!-- chunk:10 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-bai-toan-dem.html -->
## Ví dụ 10. Một nhóm công nhân gồm $15$ nam và $5$ nữ. Người ta muốn chọn từ nhóm ra $5$ người để lập thành một tổ công tác sao cho phải có $1$ tổ trưởng nam, $1$ tổ phó nam và có ít nhất $1$ nữ. Hỏi có bao nhiêu cách lập tổ công tác.

Chọn $2$ trong $15$ nam làm tổ trưởng và tổ phó có $A_{15}^{2}$ cách.

Chọn $3$ tổ viên, trong đó có nữ.

+ Chọn $1$ nữ và $2$ nam có $5.C_{13}^{2}$ cách.

+ Chọn $2$ nữ và $1$ nam có $13.C_{5}^{2}$ cách.

+ Chọn $3$ nữ có $C_{5}^{3}$ cách.

Vậy có $A_{15}^{2}\left( 5.C_{13}^{2}+13.C_{5}^{2}+C_{5}^{3} \right)=111300$ cách.

<!-- chunk:11 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-bai-toan-dem.html -->
## Ví dụ 11. Một nhóm có $5$ nam và $3$ nữ. Chọn ra $3$ người sao cho trong đó có ít nhất $1$ nữ. Hỏi có bao nhiêu cách.

Cách 1: Ta có các trường hợp sau:

• $3$ người được chọn gồm $1$ nữ và $2$ nam:

+ Chọn ra $1$ trong $3$ nữ ta có $3$ cách.

+ Chọn ra $2$ trong $5$ nam ta có $C_{5}^{2}$ cách.

Suy ra có $3C_{5}^{2}$ cách chọn.

• $3$ người được chọn gồm $2$ nữ và $1$ nam:

+ Chọn ra $2$ trong $3$ nữ có $C_{3}^{2}$ cách.

+ Chọn ra $1$ trong $5$ nam có $5$ cách.

Suy ra có $5C_{3}^{2}$ cách chọn.

• $3$ người chọn ra gồm $3$ nữ: có $1$ cách.

Vậy có $3C_{5}^{2}+5C_{3}^{2}+1=46$ cách chọn.

Cách 2: Số cách chọn $3$ người bất kì là: $C_{8}^{3}$.

Số cách chọn $3$ người nam là: $C_{5}^{3}$.

Vậy số cách chọn $3$ người thỏa yêu cầu bài toán là: $C_{8}^{3}-C_{5}^{3}=46$ cách.

<!-- chunk:12 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-bai-toan-dem.html -->
## Ví dụ 12. Một lớp có $33$ học sinh, trong đó có $7$ nữ. Cần chia lớp thành $3$ tổ, tổ 1 có $10$ học sinh, tổ 2 có $11$ học sinh, tổ 3 có $12$ học sinh sao cho trong mỗi tổ có ít nhất $2$ học sinh nữ. Hỏi có bao nhiêu cách chia như vậy?

Chia lớp thành $3$ tổ thỏa mãn yêu cầu có các trường hợp sau:

• Trường hợp 1:

+ Tổ 1 có $3$ nữ, $7$ nam có $C_{7}^{3}C_{26}^{7}$ cách chọn.

+ Tổ 2 có $2$ nữ, $9$ nam có $C_{4}^{2}C_{19}^{9}$ cách chọn.

+ Tổ 3 có $2$ nữ, $10$ nam có $C_{2}^{2}C_{10}^{10}=1$ cách chọn.

Vậy có $C_{7}^{3}C_{26}^{7}C_{4}^{2}C_{19}^{9}$ cách chia thành $3$ tổ trong trường hợp này.

• Trường hợp 2: Tổ 2 có $3$ nữ và hai tổ còn lại có $2$ nữ, tương tự tính được $C_{7}^{2}C_{26}^{8}C_{5}^{3}C_{18}^{8}$ cách chia.

• Trường hợp 3: Tổ 3 có $3$ nữ và hai tổ còn lại có $2$ nữ, tương tự tính được $C_{7}^{2}C_{26}^{8}C_{5}^{2}C_{18}^{9}$ cách chia.

Vậy có tất cả $C_{7}^{3}C_{26}^{7}C_{4}^{2}C_{19}^{9}$ $+ C_{7}^{2}C_{26}^{8}C_{5}^{3}C_{18}^{8}$ $+ C_{7}^{2}C_{26}^{8}C_{5}^{2}C_{18}^{9}$ cách chia.

<!-- chunk:13 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-bai-toan-dem.html -->
## Ví dụ 13. Một thầy giáo có $5$ cuốn sách Toán, $6$ cuốn sách Văn và $7$ cuốn sách Anh, các cuốn sách đôi một khác nhau. Thầy giáo muốn tặng $6$ cuốn sách cho $6$ học sinh. Hỏi thầy giáo có bao nhiêu cách tặng nếu:

1. Thầy giáo chỉ muốn tặng hai thể loại.

2. Thầy giáo muốn sau khi tặng xong mỗi thể loại còn lại ít nhất một cuốn.

1. Xét các trường hợp:

+ Tặng hai thể loại Toán, Văn có: $A_{11}^{6}$ cách.

+ Tặng hai thể loại Toán, Anh có: $A_{12}^{6}$ cách.

+ Tặng hai thể loại Văn, Anh có: $A_{13}^{6}$ cách.

Suy ra số cách tặng: $A_{11}^{6}+A_{12}^{6}+A_{13}^{6}=2233440$ cách.

2. Xét các trường hợp:

+ Số cách tặng hết sách Toán: $5!.13=1560$ cách.

+ Số cách tặng hết sách Văn: $6!=720$ cách.

Suy ra số cách tặng thỏa yêu cầu bài toán: $A_{18}^{6}-1560-720=13363800$ cách.

<!-- chunk:14 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-bai-toan-dem.html -->
## Ví dụ 14. Có $3$ bông hồng vàng, $3$ bông hồng trắng và $4$ bông hồng đỏ (các bông hoa đôi một khác nhau), người ta chọn ra một bó hoa gồm $7$ bông.

1. Có bao nhiêu cách chọn các bông hoa được chọn tuỳ ý.

2. Có bao nhiêu cách chọn sao cho có đúng $1$ bông màu đỏ.

3. Có bao nhiêu cách chọn sao cho có ít nhất $3$ bông hồng vàng và ít nhất $3$ bông hồng đỏ.

1. Mỗi cách chọn thỏa yêu cầu bài toán có nghĩa là ta lấy bất kì $7$ bông từ $10$ bông đã cho mà không tính đến thứ tự lấy. Do đó mỗi cách lấy là một tổ hợp chập $7$ của $10$ phần tử. Vậy số cách chọn thỏa yêu cầu bài toán là: $C_{10}^{7}=120$.

2. Có $4$ cách chọn $1$ bông hồng màu đỏ. Với mỗi cách chọn bông hồng màu đỏ, có $1$ cách chọn $6$ bông còn lại. Vậy có tất cả $4$ cách chọn bông thỏa yêu cầu bài toán.

3. Vì có tất cả $4$ bông hồng đỏ nên ta có các trường hợp sau:

• $7$ bông được chọn gồm $3$ bông vàng và $4$ bông đỏ, số cách chọn trong trường hợp này là $1$ cách.

• $7$ bông được chọn gồm $3$ bông vàng, $3$ bông đỏ và $1$ bông trắng, số cách chọn trong trường hợp này là $3.C_{4}^{3}=12$ cách.

Vậy có tất cả $13$ cách chọn thỏa yêu cầu bài toán.

**Dạng toán 3. Bài toán đếm liên quan đến hình học

**

<!-- chunk:15 level:3 source:https://toanmath.com/2018/06/phuong-phap-giai-bai-toan-dem.html -->
## Ví dụ 15. Cho hai đường thẳng song song ${d_1},{d_2}$. Trên đường thẳng ${d_1}$ lấy $10$ điểm phân biệt, trên ${d_2}$ lấy $15$ điểm phân biệt. Hỏi có bao nhiêu tam giác mà ba đỉnh của nó được chọn từ $25$ vừa nói trên.

Số tam giác lập được thuộc vào một trong hai loại sau:

• Loại 1: Gồm hai đỉnh thuộc vào ${d_1}$ và một đỉnh thuộc vào ${d_2}.$

Số cách chọn bộ hai điểm trong $10$ thuộc ${d_1}$: $C_{10}^{2}$ cách.

Số cách chọn một điểm trong $15$ điểm thuộc ${d_2}$: $C_{15}^{1}$ cách.

Suy ra loại này có: $C_{10}^{2}.C_{15}^{1}=$ tam giác.

• Loại 2: Gồm một đỉnh thuộc vào ${d_1}$ và hai đỉnh thuộc vào ${d_2}.$

Số cách chọn một điểm trong $10$ thuộc ${d_1}$: $C_{10}^{1}$ cách.

Số cách chọn bộ hai điểm trong $15$ điểm thuộc ${d_2}$: $C_{15}^{2}$ cách.

Suy ra loại này có: $C_{10}^{1}.C_{15}^{2}=$ tam giác.

Vậy có tất cả: $C_{10}^{2}C_{15}^{1}+C_{10}^{1}C_{15}^{2}$ tam giác thỏa yêu cầu bài toán.