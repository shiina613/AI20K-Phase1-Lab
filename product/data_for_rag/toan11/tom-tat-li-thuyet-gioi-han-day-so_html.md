# Tóm tắt lí thuyết giới hạn dãy số

<!-- chunk:0 level:0 source:https://toanmath.com/2020/05/tom-tat-li-thuyet-gioi-han-day-so.html -->
Bài viết trình bày tóm tắt lí thuyết giới hạn dãy số trong chương trình Đại số và Giải tích 11 chương 4: giới hạn.

<!-- chunk:1 level:1 source:https://toanmath.com/2020/05/tom-tat-li-thuyet-gioi-han-day-so.html -->
## I. GIỚI HẠN HỮU HẠN CỦA DÃY SỐ

1. Định nghĩa

Dãy số $\left( {{u_n}} \right)$ được gọi là có giới hạn bằng $0$ khi $n$ tiến ra dương vô cực nếu với mỗi số dương nhỏ tuỳ ý cho trước, mọi số hạng của dãy số, kể từ một số hạng nào đó trở đi, đều có giá trị tuyệt đối nhỏ hơn số dương đó. Kí hiệu: $\lim {u_n} = 0.$ Hay là: $\lim {u_n} = 0$ khi và chỉ khi với mọi $\varepsilon > 0$ nhỏ tùy ý, luôn tồn tại số tự nhiên ${n_0}$ sao cho: $\left| {{u_n}} \right| < \varepsilon$, $\forall n > {n_0}.$

$\lim {u_n} = a$ $\Leftrightarrow \lim \left( {{u_n} – a} \right) = 0$, tức là: Với mọi $\varepsilon > 0$ nhỏ tùy ý, luôn tồn tại số tự nhiên ${n_0}$ sao cho $\left| {{u_n} – a} \right| < \varepsilon$, $\forall n > {n_0}.$

Dãy số $\left( {{u_n}} \right)$ có giới hạn là số thực gọi là dãy số có giới hạn hữu hạn.

2. Một số giới hạn đặc biệt
$\lim \frac{1}{{{n^k}}} = 0$ với $k \in {N^*}.$

Nếu $|q| < 1$ thì $\lim {q^n} = 0.$

Nếu ${u_n} = c$ (với $c$ là hằng số) thì $\lim {u_n} = \lim c = c.$

<!-- chunk:2 level:1 source:https://toanmath.com/2020/05/tom-tat-li-thuyet-gioi-han-day-so.html -->
## II. MỘT SỐ ĐỊNH LÍ VỀ GIỚI HẠN
1. Định lí 1: Nếu dãy số $({u_n})$ thỏa mãn $\left| {{u_n}} \right| < {v_n}$ kể từ số hạng nào đó trở đi và $\lim {v_n} = 0$ thì $\lim {u_n} = 0.$

2. Định lí 2: Cho $\lim {u_n} = a$, $\lim {v_n} = b.$ Ta có:

$\lim \left( {{u_n} + {v_n}} \right) = a + b.$

$\lim \left( {{u_n} – {v_n}} \right) = a – b.$

$\lim \left( {{u_n}.{v_n}} \right) = a.b.$

$\lim \frac{{{u_n}}}{{{v_n}}} = \frac{a}{b}$ $(b \ne 0).$

Nếu ${u_n} \ge 0$ với mọi $n$ thì $\lim \sqrt {{u_n}} = \sqrt a .$

<!-- chunk:3 level:1 source:https://toanmath.com/2020/05/tom-tat-li-thuyet-gioi-han-day-so.html -->
## III. TỔNG CỦA CẤP SỐ NHÂN LÙI VÔ HẠN

Cho cấp số nhân $\left( {{u_n}} \right)$ có công bội $q$ thỏa $|q| < 1.$ Khi đó tổng $S = {u_1} + {u_2} + \ldots + {u_n} + \ldots$ gọi là tổng vô hạn của cấp số nhân và $S = \lim {S_n}$ $= \lim \frac{{{u_1}\left( {1 – {q^n}} \right)}}{{1 – q}}$ $= \frac{{{u_1}}}{{1 – q}}.$

<!-- chunk:4 level:1 source:https://toanmath.com/2020/05/tom-tat-li-thuyet-gioi-han-day-so.html -->
## IV. GIỚI HẠN VÔ CỰC

1. Định nghĩa
$\lim {u_n} = + \infty$ $\Leftrightarrow$ với mỗi số dương tuỳ ý cho trước, mọi số hạng của dãy số, kể từ một số hạng nào đó trở đi, đều lớn hơn số dương đó.

$\lim {u_n} = – \infty$ $\Leftrightarrow \lim \left( { – {u_n}} \right) = + \infty .$

2. Một số kết quả đặc biệt
$\lim {n^k} = + \infty$ với mọi $k > 0.$

$\lim {q^n} = + \infty$ với mọi $q > 1.$

3. Một vài quy tắc tìm giới hạn vô cực
Quy tắc 1: Nếu $\lim {u_n} = \pm \infty$, $\lim {v_n} = \pm \infty$ thì $\lim \left( {{u_n}{v_n}} \right)$ được cho như sau:

$\lim {u_n}$
$\lim {v_n}$
$\lim \left( {{u_n}{v_n}} \right)$

$+ \infty$
$+ \infty$
$+ \infty$

$+ \infty$
$– \infty$
$– \infty$

$– \infty$
$+ \infty$
$– \infty$

$– \infty$
$– \infty$
$+ \infty$

Quy tắc 2: Nếu $\lim {u_n} = \pm \infty$ và $\lim {v_n} = L \ne 0$ thì $\lim \left( {{u_n}{v_n}} \right)$ được cho như sau:

$\lim {u_n}$
Dấu của $L$
$\lim \left( {{u_n}{v_n}} \right)$

$+ \infty$
+ | 
$+ \infty$

$+ \infty$
– | 
$– \infty$

$– \infty$
+ | 
$– \infty$

$– \infty$
– | 
$+ \infty$

Quy tắc 3: Nếu $\lim {u_n} = L \ne 0$, $\lim {v_n} = 0$ và ${v_n} > 0$ hoặc ${v_n} < 0$ kể từ một số hạng nào đó trở đi thì $\lim \frac{{{u_n}}}{{{v_n}}}$ được cho như sau:

Dấu của $L$
Dấu của ${v_n}$
$\lim \frac{{{u_n}}}{{{v_n}}}$

$+ \infty$
+ | 
$+ \infty$

$+ \infty$
– | 
$– \infty$

$– \infty$
+ | 
$– \infty$

$– \infty$
– | 
$+ \infty$