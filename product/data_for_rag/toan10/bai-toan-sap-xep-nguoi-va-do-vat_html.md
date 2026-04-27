# Bài toán sắp xếp người và đồ vật

<!-- chunk:0 level:0 source:https://toanmath.com/2020/03/bai-toan-sap-xep-nguoi-va-do-vat.html -->
Bài viết hướng dẫn giải dạng bài toán sắp xếp người và đồ vật trong chương trình Đại số và Giải tích 11: Tổ hợp và xác suất.

1. PHƯƠNG PHÁP GIẢI TOÁN
+ Xác định số đối tượng cần sắp xếp.

+ Xác định số vị trí để sắp xếp đối tượng.

+ Dùng hoán vị hoặc chỉnh hợp hoặc tổ hợp để tính số cách sắp xếp đó.

Lưu ý:

+ Nếu có $k$ đối tượng khác nhau xếp vào $n$ $(n \ge k)$ vị trí thì có: $A_n^k$ cách sắp xếp.

+ Nếu $k$ đối tượng giống nhau xếp vào $n$ $(n \ge k)$ vị trí thì có: $C_n^k$ cách sắp xếp.

+ Một số bài toán chứa điều kiện thì có thể chia nhỏ thành các trường hợp để khi sắp xếp không bị lặp lại.

## Bài tập

## Bài 1: Một học sinh có $12$ cuốn sách đôi một khác nhau, trong đó có $2$ cuốn sách Toán, $4$ cuốn sách Văn và $6$ cuốn sách Anh. Hỏi có bao nhiêu cách xếp tất cả các cuốn sách lên một kệ sách dài, nếu các cuốn sách cùng môn được xếp kề nhau?

Lời giải:

Có $3!$ cách xếp $3$ nhóm sách (nhóm sách Toán, nhóm sách Văn, nhóm sách Anh) lên một kệ dài.

Mỗi cách xếp đó có $2!$ cách xếp $2$ cuốn sách toán, $4!$ cách xếp $4$ cuốn sách Văn và $6!$ cách xếp $6$ cuốn sách Anh.

Vậy theo quy tắc nhân có: $3!.2!.4!.6! = 207360$ cách xếp tất cả các cuốn sách lên một kệ sách dài, và các cuốn sách cùng môn được xếp kề nhau.

## Bài 2: Một bàn dài có hai dãy ghế đối diện nhau, mỗi dãy có $6$ ghế. Người ta muốn xếp chỗ ngồi cho $6$ học sinh trường A và $6$ học sinh trường B vào bàn nói trên. Hỏi có bao nhiêu cách xếp trong mỗi trường hợp sau:

## Bài tập 1. Bất cứ $2$ học sinh nào ngồi cạnh nhau hoặc đối diện nhau thì khác trường với nhau.

## Bài tập 2. Bất cứ $2$ học sinh nào ngồi đối diện nhau thì khác trường với nhau.

Lời giải:

1) Có hai sơ đồ xếp chỗ ngồi sao cho cứ $2$ học sinh nào ngồi cạnh nhau hoặc đối diện nhau thì khác trường với nhau là:

<img link="data_for_rag/toan10/images/bai-toan-sap-xep-nguoi-va-do-vat-1.png" alt="">

Mỗi sơ đồ có $6!$ cách sắp xếp $6$ học sinh trường A và $6!$ cách sắp xếp $6$ học sinh trường B.

Vậy theo quy tắc nhân có: $2.6!.6! = 1036800$ cách sắp xếp.

2) Học sinh thứ nhất trường A ngồi trước: có $12$ cách chọn ghế để ngồi.

Sau đó, chọn học sinh trường B ngồi đối diện với học sinh thứ nhất trường A: có $6$ cách chọn học sinh trường B.

Học sinh thứ hai của trường A còn $10$ chỗ để chọn, chọn học sinh trường B ngồi đối diện với học sinh thứ hai trường A: có $5$ cách chọn ..v.v..

Vậy có $12.6.10.5.8.4.6.3.4.2.2.1$ $= {2^6}.6!.6! = 33177600$ cách.

**Bài 3**: Có bao nhiêu cách sắp xếp năm bạn học sinh A, B, C, D, E vào một chiếc ghế dài sao cho:

## Bài tập 1. Bạn C ngồi chính giữa.

## Bài tập 2. Hai bạn A và E ngồi ở hai đầu ghế.

Lời giải:

1) Xếp C ngồi chính giữa có một cách xếp.

Xếp $4$ học sinh A, B, D, E vào $4$ vị trí còn lại có $4!$ cách xếp.

Vậy có: $4! = 24$ cách xếp.

2) Xếp A và E ngồi ở hai đầu ghế có $2$ cách xếp là A ngồi đầu này, E ngồi đầu kia của ghế và ngược lại.

Xếp $3$ học sinh B, C, D vào $3$ vị trí còn lại có $3!$ cách xếp.

Vậy có $2.3! = 12$ cách xếp.

## Bài 4: Có $5$ thẻ trắng và $5$ thẻ đen, đánh dấu mỗi loại theo các số $1$, $2$, $3$, $4$, $5.$ Có bao nhiêu cách sắp xếp tất cả các thẻ này thành một hàng sao cho hai thẻ cùng màu không nằm liền nhau.

Lời giải:

Có $2$ trường hợp xảy ra:

Trường hợp 1: Các thẻ trắng ở vị trí lẻ, các thẻ đen ở vị trí chẵn.

Có $5!$ cách sắp xếp $5$ thẻ trắng và $5!$ cách sắp xếp $5$ thẻ đen.

Suy ra có: $5!.5!$ cách sắp xếp.

Trường hợp 2: Các thẻ trắng ở vị trí chẵn, các thẻ đen ở vị trí lẻ.

Có $5!$ cách sắp xếp $5$ thẻ trắng và $5!$ cách sắp xếp $5$ thẻ đen.

Suy ra có $5!.5!$ cách sắp xếp.

Vậy có: $5!.5! + 5!.5! = 28800$ cách sắp xếp.

## Bài 5: Xếp $3$ viên bi đỏ có bán kính khác nhau và $3$ viên bi xanh giống nhau vào một dãy $7$ ô trống. Hỏi:

## Bài tập 1. Có bao nhiêu cách xếp khác nhau?

## Bài tập 2. Có bao nhiêu cách xếp khác nhau sao cho $3$ viên bi đỏ xếp cạnh nhau và $3$ viên bi xanh xếp cạnh nhau?

Lời giải:

## Bài tập 1. Trước hết xếp $3$ viên bi đỏ vào $7$ ô trống.

Do các viên bi đỏ khác nhau nên số cách xếp là $A_7^3.$

Sau đó xếp $3$ viên bi xanh vào $4$ ô còn lại.

Do các viên bi xanh giống nhau nên số cách xếp là $C_4^3.$

Vậy số cách xếp khác nhau là: $A_7^3.C_4^3 = 840$ cách.

## Bài tập 2. Trước hết ta cần chú ý về màu, để đỏ đứng cạnh nhau và xanh đứng cạnh nhau chỉ có $6$ cách xếp là:

ĐĐĐXXX▯, ĐĐĐ▯XXX, ▯ĐĐĐXXX, XXXĐĐĐ▯, XXX▯ĐĐĐ, ▯XXXĐĐĐ.

Sau đó, do các viên bi đỏ khác nhau, nên mỗi cách sắp xếp $3$ bi đỏ là một hoán vị các viên bị đỏ với nhau.

Suy ra số cách sắp xếp $3$ bi đỏ là $3!.$

Và $3$ bi xanh giống nhau nên chỉ có $1$ cách sắp xếp.

Vậy số cách xếp khác nhau để các viên bi đỏ đứng cạnh nhau và các viên bi xanh đứng cạnh nhau là: $6.3! = 36$ cách.

## Bài 6: Một nhóm gồm $10$ học sinh, trong đó có $7$ nam và $3$ nữ. Hỏi có bao nhiêu cách sắp xếp $10$ học sinh trên thành một hàng dài sao cho $7$ học sinh nam phải đứng liền nhau.

Lời giải:

Coi $7$ học sinh nam đứng liền nhau như một vị trí, đặt $a$ là vị trí của $7$ học sinh nam thì số cách để bố trí $a$ đứng liền nhau xen kẽ với $3$ học sinh nữ bằng $4!.$ Nhưng để xếp $7$ học sinh nam đứng liền nhau thì lại có $7!$ cách.

Vậy tất cả có: $4!7! = 120960$ cách.

## Bài 7: Có $6$ học sinh nam và $3$ học sinh nữ xếp thành một hàng dọc. Hỏi có bao nhiêu cách xếp để có đúng $2$ học sinh nam đứng xen kẽ $3$ học sinh nữ (khi đổi chỗ $2$ học sinh bất kì cho nhau ta được một cách xếp mới).

Lời giải:

Đánh số vị trí đứng từ $1$ đến $9.$

Để có đúng $2$ học sinh nam đứng xen kẽ với $3$ học sinh nữ thì mỗi học sinh nữ đứng cách nhau một, tức là $3$ học sinh nữ đứng ở các vị trí $(1;3;5)$; $(2;4;6)$; $(3;5;7)$; $(4;6;8)$; $(5;7;9).$

Có $5$ cặp $3$ vị trí của $3$ học sinh nữ.

Cách xếp $3$ bạn nữ vào mỗi cặp $3$ vị trí là $3!.$ Cách xếp $6$ bạn nam vào $6$ vị trí còn lại là $6!.$

Vậy tất cả số cách xếp là: $5.3!.6! = 21600$ cách.

## Bài 8: Một bàn dài gồm $6$ ghế được đánh số từ $1$ đến $6.$ Xếp $3$ nam và $3$ nữ ngồi sao cho số $1$ và số $2$ là nữ. Hỏi có bao nhiêu cách xếp như trên.

Lời giải:

Chọn $2$ nữ xếp vào vị trí số $1$ và số $2$ có: $A_3^2 = 6$ cách chọn.

Số các xếp $3$ nam và $1$ nữ còn lại có $4! = 24$ cách xếp.

Vậy có: $6.24 = 144$ cách xếp thỏa yêu cầu bài toán.

## Bài 9: Có $12$ đội bóng tham gia tranh giải vô địch quốc gia. Trong vòng đấu loại các đối thủ đấu với nhau theo thể thức vòng tròn, hai đội bóng bất kỳ gặp nhau hai trận, một trận lượt đi và một trận lượt về. Hỏi có bao nhiêu trận đấu trong vòng loại?

Lời giải:

Mỗi đội bóng bất kỳ thì $11$ trận đấu với $11$ đội bóng còn lại.

Suy ra số trận đấu là: $12.11 = 132$ trận.

Cách khác:

Số cách chọn $2$ đội bóng bất kỳ thì có $2$ trận đấu lượt đi hoặc lượt về.

Do đó số trận đấu trong vòng bảng là: $A_{12}^2 = 132$ trận.

## Bài 10: Một thầy giáo có $12$ cuốn sách đôi một khác nhau trong đó có $5$ cuốn sách Văn, $4$ cuốn sách Nhạc và $3$ cuốn sách Họa. Ông muốn lấy ra $6$ cuốn và tặng cho $6$ học sinh A, B, C, D, E, F mỗi em một cuốn.

## Bài tập 1. Giả sử thầy giáo chỉ muốn tặng cho các học sinh trên những cuốn sách thuộc $2$ thể loại Văn và Nhạc. Hỏi có bao nhiêu cách tặng?

## Bài tập 2. Giả sử thầy giáo muốn rằng sau khi tặng sách xong, mỗi một trong ba loại sách trên đều còn lại ít nhất một cuốn. Hỏi có bao nhiêu cách chọn?

Lời giải:

## Bài tập 1. Số cách tặng là số cách chọn $6$ cuốn sách từ $9$ cuốn có kể thứ tự, tức là mỗi cách chọn là một chỉnh hợp chập $6$ của $9.$

Vậy số cách tặng là $A_9^6 = 60480.$

## Bài tập 2. Nhận xét: không thể chọn sao cho cùng hết $2$ loại sách.

Số cách chọn $6$ cuốn sách từ $12$ cuốn sách là: $A_{12}^6 = 66528.$

Số cách chọn sao cho không còn sách Văn là: $A_5^5.A_7^1 = 840.$

Số cách chọn sao cho không còn sách Nhạc là: $A_4^4.A_8^2 = 1344.$

Số cách chọn sao cho không còn sách Hoạ là: $A_3^3.A_9^3 = 3024.$

Số cách chọn cần tìm là: $66528 – (840 + 1344 + 3024) = 660072.$

## Bài 11: Một lớp có $18$ nam và $12$ nữ. Có bao nhiêu cách chọn $5$ bạn làm ban cán sự lớp sao cho:

a) Mọi người đều vui vẻ tham gia.

b) Bạn A và B không thể làm việc chung với nhau.

c) Bạn C và D từ chối tham gia.

Lời giải:

a) Tổng số có $18 + 12 = 30$ học sinh trong lớp.

Chọn $5$ bạn thì số cách chọn là: $C_{30}^5 = 142506$ cách.

b) Xét các trường hợp sau:

+ Chọn $5$ bạn trong đó có bạn A và không có bạn B.

Chọn A có $1$ cách chọn.

Chọn $4$ bạn khác A, B có $C_{28}^4 = 20475$ cách chọn.

Suy ra trường hợp này có $20475$ cách chọn.

+ Chọn $5$ bạn trong đó có bạn B và không có bạn A.

Chọn B có $1$ cách chọn.

Chọn $4$ bạn khác A, B có $C_{28}^4 = 20475$ cách chọn.

Suy ra trường hợp này có $20475$ cách chọn.

+ Chọn $5$ bạn trong đó không có cả hai bạn A và B thì có: $C_{28}^5 = 98280$ cách chọn.

Vậy tất cả có $20475 + 20475 + 98280 = 1139230$ cách chọn ban cán sự lớp gồm $5$ bạn trong đó A và B không đồng thời có mặt.

Cách khác:

Số cách chọn trong đó A và B đồng thời nằm trong ban cán sự lớp là: $C_{28}^3 = 3276$ cách.

Vậy số cách chọn cần tìm là: $142506 – 3276 = 1139230$ cách.

c) Số cách chọn là: $C_{28}^5 = 98280.$

## Bài 12: Có $5$ nam và $5$ nữ ngồi vào hai dãy ghế đối diện nhau, mỗi dãy có $5$ ghế. Hỏi:

a) Có bao nhiêu cách sắp xếp sao cho hai người đối diện khác phái?

b) Có bao nhiêu cách sắp xếp mà nam nữ ngồi xen kẽ và đối diện?

Lời giải:

a) Học sinh nam thứ nhất có $10$ cách chọn chỗ ngồi, sau đó chọn $1$ học sinh nữ ngồi đối diện với học sinh nam đã chọn có $5$ cách.

Học sinh nam thứ hai có $8$ cách chọn chỗ ngồi, chọn $1$ học sinh nữ ngồi đối diện có $4$ cách.

Học sinh nam thứ ba có $6$ cách chọn chỗ ngồi, chọn $1$ học sinh nữ ngồi đối diện có $3$ cách.

Học sinh nam thứ tư có $4$ cách chọn chỗ ngồi, chọn $1$ học sinh nữ ngồi đối diện có $2$ cách.

Học sinh nam thứ hai có $2$ cách chọn chỗ ngồi, chọn $1$ học sinh nữ ngồi đối diện có $1$ cách.

Vậy có $10.5.8.4.6.3.4.2.2.1 = {2^5}.5!.5! = 460800$ cách sắp xếp để hai người đối diện khác phái.

Cách khác:

Chọn cặp nam, nữ thứ nhất và xếp vào $2$ ghế đối diện đã chọn có $2.5.5$ cách chọn (có thể nam_nữ hoặc nữ_nam).

Chọn cặp nam, nữ thứ hai và xếp vào $2$ ghế đối diện đã chọn có $2.4.4$ cách chọn (có thể nam_nữ hoặc nữ_nam).

Chọn cặp nam, nữ thứ ba và xếp vào $2$ ghế đối diện đã chọn có $2.3.3$ cách chọn (có thể nam_nữ hoặc nữ_nam).

Chọn cặp nam, nữ thứ tư và xếp vào $2$ ghế đối diện đã chọn có $2.2.2$ cách chọn (có thể nam_nữ hoặc nữ_nam).

Chọn cặp nam, nữ thứ năm và xếp vào $2$ ghế đối diện đã chọn có $2.1.1$ cách chọn (có thể nam_nữ hoặc nữ_nam).

Vậy có $2.5.5.2.4.4.2.3.3.2.2.2.2.1.1 = 460800$ cách.

b) Có $2$ sơ đồ để sắp xếp nam nữ đối diện và xen kẽ là: (ký hiệu B: nam và G: nữ).

<img link="data_for_rag/toan10/images/bai-toan-sap-xep-nguoi-va-do-vat-2.png" alt="">

Mỗi sơ đồ có $5!$ cách sắp xếp $5$ nam và $5!$ cách sắp xếp $5$ nữ.

Vậy có $2.5!.5! = 28800$ cách sắp xếp nam nữ ngồi xen kẽ và đối diện.

## Bài 13: Một tổ gồm $6$ nam và $4$ nữ. Có bao nhiêu cách xếp hàng sao cho các bạn nữ đứng thành $2$ cặp và $2$ cặp này không đứng cạnh nhau?

Lời giải:
Chọn nhóm A gồm $2$ nữ là $C_4^2$ cách chọn.

$2$ nữ còn lại là nhóm B có $1$ cách chọn.

Suy ra có $C_4^2 = 6$ cách chia $4$ nữ thành $2$ nhóm A và B (mỗi nhóm $2$ nữ).

Mỗi cách chia trên có $8!$ cách xếp nhóm A, B và $6$ bạn nam. Và có $2!$ cách xếp $2$ nữ trong nhóm A, $2!$ cách xếp $2$ nữ trong nhóm B.

Vậy có $6.8!.2!.2! = 967680$ cách sắp xếp $6$ nam và $4$ nữ theo một hàng sao cho nữ đứng thành $2$ cặp.

Mặt khác khi hoán đổi vị trí cho nhau thì số nữ sẽ được tính lặp lại $2$ lần do đó số cách sắp xếp là:

$967680:2 = 483840$ cách.

Trong các cách trên ta xét trường hợp $4$ nữ đứng cạnh nhau.

Gọi C là khối thống nhất của $4$ nữ đứng cạnh nhau.

Có $7!$ cách xếp C và $6$ bạn nam.

Mỗi cách xếp như trên có $4!$ cách xếp $4$ bạn nữ trong khối C.

Suy ra có: $7!.4! = 120960$ cách xếp để $4$ nữ đứng cạnh nhau.

Vậy có $483840 – 120960 = 362880$ cách xếp thỏa mãn yêu cầu bài toán.

Cách khác:

Giả sử xếp $6$ nam và $4$ nữ thành hàng theo số thứ tự:

<img link="data_for_rag/toan10/images/bai-toan-sap-xep-nguoi-va-do-vat-3.png" alt="">

Ta tính số trường hợp xảy ra như sau:

+ Nếu $2$ nữ xếp vào vị trí $1\_2$ thì $2$ nữ còn lại có $6$ cách chọn vị trí ($3\_4$; $4\_5$; $5\_6$; ${6\_7}$; ${7\_8}$; ${8\_9}$; ${9\_10}$).

+ Nếu $2$ nữ xếp vào vị trí $2\_3$ thì $2$ nữ còn lại có $5$ cách xếp vào $2$ vị trí liền nhau mà không trùng với trường hợp trên.

+ Nếu $2$ nữ xếp vào vị trí $3\_4$ thì $2$ nữ còn lại có $4$ cách xếp vào $2$ vị trí liền nhau mà không trùng $2$ trường hợp trên.

… … …

+ Nếu $2$ nữ xếp vào vị trí $6\_7$ thì $2$ nữ còn lại có $1$ cách xếp vào vị trí $9\_10.$

Suy ra có tất cả $6 + 5 + 4 + 3 + 2 + 1 = 21$ trường hợp để nữ xếp thành $2$ cặp và $2$ cặp này không đứng cạnh nhau.

Mỗi trường hợp có $4! = 24$ cách xếp $4$ nữ và $6! = 720$ cách xếp $6$ nam.

Vậy có $21.24.720=362880$ cách xếp thỏa mãn yêu cầu bài toán.

## Bài 14: Cần xếp $3$ nam và $2$ nữ vào $1$ hàng ghế có $7$ chỗ ngồi sao cho $3$ nam ngồi kề nhau và $2$ nữ ngồi kề nhau. Hỏi có bao nhiêu cách.

Lời giải:

Giả sử ghế có $7$ chỗ ngồi như sau: ▯▯▯▯▯▯▯.

Đầu tiên ta coi $3$ nam là một khối thống nhất là $a$ và $2$ nữ là một khối thống nhất là $b$ và $c$ là $2$ ghế trống còn lại.

+ Hoán vị $2$ khối $a$, $b$ và $c$ có $3!$ cách.

+ Có $3!$ cách sắp xếp $3$ nam của khối $a$ và $2!$ cách xếp $2$ nữ của khối $b.$

+ $c$ gồm $2$ ghế không phân biệt nên chỉ có $1$ cách.

Vậy có $3!.3!.2! = 72$ cách sắp xếp.

## Bài 15: Mỗi người sử dụng hệ thống máy tính đều có mật khẩu dài từ $6$ đến $8$ ký tự, trong đó mỗi ký tự là một chữ hoa hay chữ số. Mỗi mật khẩu phải chứa ít nhất một chữ số. Hỏi mỗi người có thể có bao nhiêu mật khẩu? Biết rằng có $26$ chữ in hoa, $10$ chữ số.

Lời giải:

Gọi $P$ là tổng số mật khẩu có thể và ${P_6}$, ${P_7}$, ${P_8}$ tương ứng là số mật khẩu dài $6$, $7$, $8$ ký tự. Theo quy tắc cộng ta có: $P = {P_6} + {P_7} + {P_8}.$

+ Tính ${P_6}$:

Số xâu dài $6$ ký tự là chữ in hoa hoặc chữ số là: ${36^6}$ vì mỗi vị trí có $36$ cách chọn.

Số xâu dài $6$ ký tự là chữ in hoa và không chứa chữ số nào là: ${26^6}.$

Vậy: ${P_6} = {36^6} – {26^6}.$

+ Tương tự: ${P_7} = {36^7} – {26^7}$ và ${P_8} = {36^8} – {26^8}.$

Vậy ta được: $P = {P_6} + {P_7} + {P_8}$ $= 2684483063360.$

## Bài 16: Có bao nhiêu cách chọn $4$ cầu thủ khác nhau trong $10$ cầu thủ của đội bóng quần vợt để chơi bốn trận đấu đơn, các trận đấu là có thứ tự?

Lời giải:

Mỗi cách chọn bốn cầu thủ của đội bóng là một chỉnh hợp chập $4$ của $10$ phần tử.

Ta có: $A_{10}^4 = 5040$ cách chọn.

## Bài 17: Người ta xếp ngẫu nhiên $5$ lá phiếu từ $1$ đến $5$ cạnh nhau.

a) Có bao nhiêu cách sắp xếp để các phiếu số chẵn luôn ở cạnh nhau .

b) Có bao nhiêu cách xếp để các phiếu phân thành các nhóm chẵn lẻ riêng biệt.

Lời giải:

Giả sử $2$ lá phiếu chẵn đứng cạnh nhau là một khối thống nhất $A.$

Xếp khối $A$ và $3$ lá phiếu còn lại có $4!$ cách xếp.

Xếp $2$ lá phiếu trong khối A có $2!$ cách xếp.

Vậy có $4!.2! = 48$ cách xếp.

b) Có $2$ trường hợp để xếp $5$ lá phiếu thành hai nhóm riêng biệt đó là các phiếu chẵn ở bên trái và các phiếu lẻ ở phía bên phải và ngược lại.

Mỗi trường hợp có $3!$ cách xếp $3$ phiếu lẻ và $2!$ cách xếp $2$ phiếu chẵn.

Vậy có $2.3!.2! = 24$ cách xếp.