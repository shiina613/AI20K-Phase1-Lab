# Các tích phân đặc biệt

<!-- chunk:0 level:0 source:https://toanmath.com/2020/03/cac-tich-phan-dac-biet.html -->
Trong chủ đề này chúng ta cùng nhau đi chứng minh rồi áp dụng một số tính chất cho những lớp tích phân đặc biệt.

Tính chất 1: Nếu $f(x)$ liên tục và là hàm lẻ trên $\left[ { – a;a} \right]$ thì: $I = \int_{ – a}^a f (x)dx = 0.$

Chứng minh:

Biến đổi $I$ về dạng:

$I = \int_{ – a}^a f (x)dx$ $= \int_{ – a}^0 f (x)dx + \int_0^a f (x)dx$ $(1).$

Xét tính phân $J = \int_{ – a}^0 f (x)dx.$

Đặt $x = – t$ $\Rightarrow dx = – dt.$

Đổi cận: $x = – a$ $\Rightarrow t = a$, $x = 0$ $\Rightarrow t = 0.$

Mặt khác vì $f(x)$ là hàm lẻ $\Rightarrow f( – t) = – f(t).$

Khi đó:

$J = – \int_a^0 f ( – t)dt$ $= – \int_0^a f (t)dt$ $= – \int_0^a f (x)dx$ $(2).$

Thay $(2)$ vào $(1)$ ta được $I= 0.$

<!-- chunk:1 level:3 source:https://toanmath.com/2020/03/cac-tich-phan-dac-biet.html -->
## Ví dụ 1: Tính tích phân: $I = \int_{ – 1/2}^{1/2} {\cos x.\ln \left( {\frac{{1 – x}}{{1 + x}}} \right)dx} .$

Lời giải:

Nhận xét rằng: Hàm số $f(x) = \cos x.\ln \left( {\frac{{1 – x}}{{1 + x}}} \right)$ có:

+ Liên tục trên $\left[ { – \frac{1}{2};\frac{1}{2}} \right].$

+ Ta có nhận xét:

$f(x) + f( – x)$ $= \cos x.\ln \left( {\frac{{1 – x}}{{1 + x}}} \right)$ $+ \cos ( – x).\ln \left( {\frac{{1 + x}}{{1 – x}}} \right).$

$= \left[ {\ln \left( {\frac{{1 – x}}{{1 + x}}} \right) + \ln \left( {\frac{{1 + x}}{{1 – x}}} \right)} \right]\cos x$ $= \ln 1.\cos x = 0.$

$\Rightarrow f( – x) = – f(x).$

Vậy $f(x)$ là hàm lẻ trên $\left[ { – \frac{1}{2};\frac{1}{2}} \right]$, do đó theo tính chất 1 ta được $I = 0.$

Chú ý quan trọng:

1. Khi gặp dạng tích phân trên thông thường học sinh nghĩ ngay tới phương pháp tích phân từng phần, xong đó lại không phải ý kiến hay. Điều đó cho thấy việc nhìn nhận tính chất cận và đặc tính của hàm số dưới dấu tích phân để từ đó định hướng việc lựa chọn phương pháp giải là rất quan trọng.

2. Tuy nhiên với một bài thi thì vì tính chất 1 không được trình bày trong phạm vi kiến thức của sách giáo khoa do đó các em học sinh nên trình bày như sau:

$I = \int_{ – 1/2}^0 {\cos x.\ln \left( {\frac{{1 – x}}{{1 + x}}} \right)dx}$ $+ \int_0^{1/2} {\cos x.\ln \left( {\frac{{1 – x}}{{1 + x}}} \right)dx.}$

Xét tính phân $J = \int_{ – 1/2}^0 {\cos x.\ln \left( {\frac{{1 – x}}{{1 + x}}} \right)dx} .$

Đặt $x = – t$ $\Rightarrow dx = – dt.$

Đổi cận: $x = – \frac{1}{2}$ $\Rightarrow t = \frac{1}{2}$, $x = 0$ $\Rightarrow t = 0.$

Khi đó: $I = – \int_{1/2}^0 {\cos ( – t)\ln \left( {\frac{{1 + t}}{{1 – t}}} \right)dt}$ $= – \int_0^{1/2} {\cos t\ln \left( {\frac{{1 – t}}{{1 + t}}} \right)dt} .$

$= – \int_0^{1/2} {\cos x.\ln \left( {\frac{{1 – x}}{{1 + x}}} \right)dx} .$

Thay $(2)$ vào $(1)$ ta được $I = 0.$

3. Vậy kể từ đây trở đi chúng ta sẽ đi áp dụng ý tưởng trong phương pháp chứng minh tính chất để giải ví dụ trong mục áp dụng.

Tính chất 2: Nếu $f(x)$ liên tục và là hàm chẵn trên đoạn $\left[ { – a;a} \right]$ thì: $I = \int_{ – a}^a f (x)dx$ $= 2\int_0^a f (x)dx.$

Chứng minh:

Biến đổi $I$ về dạng:

$I = \int_{ – a}^a f (x)dx$ $= \int_{ – a}^0 f (x)dx + \int_0^a f (x)dx$ $(1).$

Xét tính phân $J = \int_{ – a}^0 f (x)dx.$

Đặt $x = – t$ $\Rightarrow dx = – dt.$

Đổi cận: $x = – a \Rightarrow t = a$, $x = 0 \Rightarrow t = 0.$

Mặt khác vì $f(x)$ là hàm chẵn $\Rightarrow f( – t) = f(t).$

Khi đó: $J = – \int_a^0 f ( – t)dt$ $= \int_0^a f (t)dt = \int_0^a f (x)dx$ $(2).$

Thay $(2)$ vào $(1)$ ta được $I = 2\int_0^a f (x)dx.$

Chú ý quan trọng:

1. Trong phạm vi phổ thông tính chất trên không mang nhiều ý nghĩa ứng dụng, do đó khi gặp các bài toán kiểu này chúng ta tốt nhất cứ đi xác định $I = \int_{ – a}^a f (x)dx$ bằng cách thông thường, thí dụ với tích phân:

$I = \int_{ – 1}^1 {{x^2}dx} .$

Ta không nên sử dụng phép biến đổi:

$I = 2\int_0^1 {{x^2}dx}$ $= \left. {\frac{{2{x^3}}}{3}} \right|_0^1 = \frac{2}{3}.$

Bởi khi đó ta nhất thiết cần đi chứng minh lại tính chất 2, điều này khiến bài toán trở lên cồng kềnh hơn nhiều so với cách làm thông thường, cụ thể:

$I = \left. {\frac{{{x^3}}}{3}} \right|_{ – 1}^1 = \frac{2}{3}.$

2. Tuy nhiên không thể phủ nhận sự tiện lợi của nó trong một vài trường hợp rất đặc biệt.

Tính chất 3: Nếu $f(x)$ liên tục và chẵn trên $R$ thì $I = \int_{ – \alpha }^\alpha {\frac{{f(x)dx}}{{{a^x} + 1}}}$ $= \int_0^\alpha f (x)dx$ với mọi $\alpha \in {R^ + }$ và $a > 0.$

Chứng minh:

Biến đổi $I$ về dạng:

$I = \int_{ – \alpha }^\alpha {\frac{{f(x)dx}}{{{a^x} + 1}}}$ $= \int_{ – \alpha }^0 {\frac{{f(x)dx}}{{{a^x} + 1}}} + \int_0^\alpha {\frac{{f(x)dx}}{{{a^x} + 1}}} .$

Xét tính phân ${I_1} = \int_{ – \alpha }^0 {\frac{{f(x)dx}}{{{a^x} + 1}}} .$

Đặt $x = – t$ $\Rightarrow dx = – dt.$

Đổi cận: $x = – \alpha \Rightarrow t = \alpha$, $x = 0 \Rightarrow t = 0.$

Mặt khác vì $f(x)$ là hàm chẵn $\Rightarrow f( – t) = f(t).$

Khi đó: ${I_1} = – \int_\alpha ^0 {\frac{{f( – t)dt}}{{{a^{ – t}} + 1}}}$ $= \int_0^\alpha {\frac{{{a^t}f(t)dt}}{{{a^t} + 1}}}$ $= \int_0^\alpha {\frac{{{a^t}f(t)dt}}{{{a^t} + 1}}} .$

Vậy: $I = \int_0^\alpha {\frac{{{a^t}f(t)dt}}{{{a^t} + 1}}} + \int_0^\alpha {\frac{{f(x)dx}}{{{a^x} + 1}}}$ $= \int_0^\alpha {\frac{{\left( {{a^x} + 1} \right)f(x)dx}}{{{a^x} + 1}}}$ $= \int_0^\alpha f (x)dx.$

<!-- chunk:2 level:3 source:https://toanmath.com/2020/03/cac-tich-phan-dac-biet.html -->
## Ví dụ 2: Tính tích phân: $I = \int_{ – 1}^1 {\frac{{{x^4}dx}}{{{2^x} + 1}}} .$

Lời giải:

Biến đổi $I$ về dạng:

$I = \int_{ – 1}^0 {\frac{{{x^4}dx}}{{{2^x} + 1}}} + \int_0^1 {\frac{{{x^4}dx}}{{{2^x} + 1}}}$ $(1).$

Xét tính phân $J = \int_{ – 1}^0 {\frac{{{x^4}dx}}{{{2^x} + 1}}} .$

Đặt $x = – t \Rightarrow dx = – dt.$

Đổi cận: $x = – 1 \Rightarrow t = 1$, $x = 0 \Rightarrow t = 0.$

Khi đó: $J = – \int_1^0 {\frac{{{{( – t)}^4}dt}}{{{2^{ – t}} + 1}}}$ $= \int_0^1 {\frac{{{t^4}{{.2}^t}dt}}{{{2^t} + 1}}} = \int_0^1 {\frac{{{x^4}{{.2}^x}dx}}{{{2^x} + 1}}}$ $(2).$

Thay $(2)$ vào $(1)$ ta được:

$I = \int_0^1 {\frac{{{x^4}{{.2}^x}dx}}{{{2^x} + 1}}} + \int_0^1 {\frac{{{x^4}dx}}{{{2^x} + 1}}}$ $= \int_0^1 {\frac{{{x^4}\left( {{2^x} + 1} \right)dx}}{{{2^x} + 1}}}$ $= \int_0^1 {{x^4}} dx = \frac{1}{5}.$

Tính chất 4: Nếu $f(x)$ liên tục trên $\left[ {0;\frac{\pi }{2}} \right]$ thì $\int_0^{\pi /2} f (\sin x)dx = \int_0^{\pi /2} f (\cos x)dx.$

Chứng minh:

Đặt $t = \frac{\pi }{2} – x$ $\Rightarrow dx = – dt.$

Đổi cận: $x = 0 \Rightarrow t = \frac{\pi }{2}$, $x = \frac{\pi }{2} \Rightarrow t = 0.$

Khi đó: $\int_0^{\pi /2} f (\sin x)dx$ $= – \int_{\pi /2}^0 {f\left( {\sin \left( {\frac{\pi }{2} – t} \right)} \right)dt}$ $= \int_0^{\pi /2} f (\cos t)dt$ $= \int_0^{\pi /2} f (\cos x)dx.$

Chú ý quan trọng: Như vậy việc áp dụng tính chất 4 để tính tích phân $I = \int_0^{\pi /2} f (\sin x)dx$ (hoặc $I = \int_0^{\pi /2} f (\cos x)dx$) thường được thực hiện theo các bước sau:

+ Bước 1: Bằng phép đổi biến $t = \frac{\pi }{2} – x$ như trong phần chứng minh tính chất, ta thu được: $I = \int_0^{\pi /2} f (\cos x)dx.$

+ Bước 2: Đi xác định $kI$ (nó được phân tích $kI = \alpha \int_0^{\pi /2} f (\sin x)dx + \beta \int_0^{\pi /2} f (\cos x)dx$), thường là:

$2I = \int_0^{\pi /2} f (\sin x)dx + \int_0^{\pi /2} f (\cos x)dx$ $\int_0^{\pi /2} {\left[ {f(\sin x) + f(\cos x)} \right]dx} .$ Từ đó suy ra giá trị của $I.$

<!-- chunk:3 level:3 source:https://toanmath.com/2020/03/cac-tich-phan-dac-biet.html -->
## Ví dụ 3: Tính tích phân: $I = \int_0^{\pi /2} {\frac{{{{\cos }^n}xdx}}{{{{\cos }^n}x + {{\sin }^n}x}}} .$

Lời giải:

Đặt $t = \frac{\pi }{2} – x$ $\Rightarrow dx = – dt.$

Đổi cận: $x = 0 \Rightarrow t = \frac{\pi }{2}$, $x = \frac{\pi }{2} \Rightarrow t = 0.$

Khi đó: $I = \int_{\pi /2}^0 {\frac{{{{\cos }^n}\left( {\frac{\pi }{2} – t} \right)( – dt)}}{{{{\cos }^n}\left( {\frac{\pi }{2} – t} \right) + {{\sin }^n}\left( {\frac{\pi }{2} – t} \right)}}}$ $= \int_0^{\pi /2} {\frac{{{{\sin }^n}tdt}}{{{{\cos }^n}t + {{\sin }^n}t}}}$ $= \int_0^{\pi /2} {\frac{{{{\sin }^n}x}}{{{{\cos }^n}x + {{\sin }^n}x}}dx.}$

Do đó: $2I = \int_0^{\pi /2} {\frac{{{{\cos }^n}x + {{\sin }^n}x}}{{{{\cos }^n}x + {{\sin }^n}x}}dx}$ $= \int_0^{\pi /2} d x = \frac{\pi }{2}$ $\Rightarrow I = \frac{\pi }{4}.$

Tính chất 5: Nếu $f(x)$ liên tục và $f(a + b – x) = f(x)$ thì: $I = \int_a^b x f(x)dx$ $= \frac{{a + b}}{2}\int_a^b f (x)dx.$

Chứng minh:

Đặt $x = a + b – t$ $\Rightarrow dx = – dt.$

Đổi cận: $x = a \Rightarrow t = b$, $x = b \Rightarrow t = a.$

Khi đó:

$I = \int_b^a {(a + b – t)} f(a + b – t)( – dt)$ $= \int_a^b {(a + b – t)} f(t)dt.$

$= \int_a^b {(a + b)} f(t)dt – \int_a^b t f(t)dt$ $= (a + b)\int_a^b f (t)dt – \int_a^b x f(x)dx.$

$= (a + b)\int_a^b f (t)dt – I.$

$\Leftrightarrow 2I = (a + b)\int_a^b f (t)dt$ $\Leftrightarrow I = \frac{{a + b}}{2}\int_a^b f (x)dx.$

Hệ quả 1: Nếu $f(x)$ liên tục trên $[0;1]$ thì: $I = \int_\alpha ^{\pi – \alpha } x f(\sin x)dx$ $= \frac{\pi }{2}\int_\alpha ^{\pi – \alpha } f (\sin x)dx.$

Chứng minh:

Hướng dẫn: Đặt $x = \pi – t$ $\Rightarrow dx = – dt.$

<!-- chunk:4 level:3 source:https://toanmath.com/2020/03/cac-tich-phan-dac-biet.html -->
## Ví dụ 4: Tính tích phân $I = \int_0^\pi {\frac{{x\sin xdx}}{{4 – {{\cos }^2}x}}} .$

Lời giải:

Biến đổi $I$ về dạng:

$I = \int_0^\pi {\frac{{x\sin xdx}}{{4 – \left( {1 – {{\sin }^2}x} \right)}}}$ $= \int_0^\pi {\frac{{x\sin xdx}}{{3 + {{\sin }^2}x}}}$ $= \int_0^\pi x f(\sin x)dx.$

Đặt $x = \pi – t$ $\Rightarrow dx = – dt.$

Đổi cận: $x = \pi \Rightarrow t = 0$, $x = 0 \Rightarrow t = \pi .$

Khi đó: $I = – \int_\pi ^0 {\frac{{(\pi – t)\sin (\pi – t)dt}}{{4 – {{\cos }^2}(\pi – t)}}}$ $= \int_0^\pi {\frac{{(\pi – t)\sin tdt}}{{4 – {{\cos }^2}t}}}$ $= \int_0^\pi {\frac{{\pi \sin tdt}}{{4 – {{\cos }^2}t}}} – \int_0^\pi {\frac{{t\sin tdt}}{{4 – {{\cos }^2}t}}} .$

$= – \pi \int_0^\pi {\frac{{d(\cos t)}}{{4 – {{\cos }^2}t}}} – I$ $\Leftrightarrow 2I = – \pi \int_0^\pi {\frac{{d(\cos t)}}{{4 – {{\cos }^2}t}}}$ $= \pi \int_0^\pi {\frac{{d(\cos t)}}{{{{\cos }^2}t – 4}}} .$

$\Leftrightarrow I = \frac{\pi }{2}\int_0^\pi {\frac{{d(\cos t)}}{{{{\cos }^2}t – 4}}}$ $= \frac{\pi }{2}.\frac{1}{4}\left. {\ln \left| {\frac{{\cos t – 2}}{{\cos t + 2}}} \right|} \right|_0^\pi$ $= \frac{{\pi \ln 9}}{8}.$

Hệ quả 2: Nếu $f(x)$ liên tục trên $[0;1]$ thì: $I = \int_\alpha ^{2\pi – \alpha } x f(\cos x)dx$ $= \pi \int_\alpha ^{2\pi – \alpha } f (\cos x)dx.$

Chứng minh:

Hướng dẫn: Đặt $x = 2\pi – t$ $\Rightarrow dx = – dt.$

<!-- chunk:5 level:3 source:https://toanmath.com/2020/03/cac-tich-phan-dac-biet.html -->
## Ví dụ 5: Tính tích phân: $I = \int_0^{2\pi } x .{\cos ^3}xdx.$

Lời giải:

Đặt $x = 2\pi – t$ $\Rightarrow dx = – dt.$

Đổi cận: $x = 2\pi \Rightarrow t = 0$, $x = 0 \Rightarrow t = 2\pi .$

Khi đó: $I = \int_{2\pi }^0 {(2\pi – t)} {\cos ^3}(2\pi – t)( – dt)$ $= \int_0^{2\pi } {(2\pi – t)} {\cos ^3}tdt.$

$= 2\pi \int_0^{2\pi } {{{\cos }^3}} tdt – \int_0^{2\pi } t {\cos ^3}tdt$ $= \frac{\pi }{2}\int_0^{2\pi } {(\cos 3t + 3\cos t)dt} – I.$

$\Leftrightarrow 2I = \left. {\frac{\pi }{2}\left( {\frac{1}{3}\sin 3t + 3\sin t} \right)} \right|_0^{2\pi } = 0$ $\Leftrightarrow I = 0.$

Tính chất 6: Nếu $f(x)$ liên tục và $f(a + b – x) = – f(x)$ thì $I = \int_a^b f (x)dx = 0.$

Chứng minh:

Đặt $x = a + b – t$ $\Rightarrow dx = – dt.$

Đổi cận: $x = a \Rightarrow t = b$, $x = b \Rightarrow t = a.$

Khi đó: $I = \int_b^a f (a + b – t)( – dt)$ $= – \int_a^b f (t)dt$ $= – \int_a^b f (x)dx = – I$ $\Leftrightarrow 2I = 0$ $\Leftrightarrow I = 0.$

<!-- chunk:6 level:3 source:https://toanmath.com/2020/03/cac-tich-phan-dac-biet.html -->
## Ví dụ 6: Tính tích phân: $I = \int_0^{\pi /2} {\ln } \left( {\frac{{1 + \sin x}}{{1 + \cos x}}} \right)dx.$

Lời giải:

Đặt $t = \frac{\pi }{2} – x$ $\Rightarrow dx = – dt.$

Đổi cận: $x = 0 \Rightarrow t = \frac{\pi }{2}$, $x = \frac{\pi }{2} \Rightarrow t = 0.$

Khi đó: $I = \int_{\pi /2}^0 {\ln } \left( {\frac{{1 + \sin \left( {\frac{\pi }{2} – t} \right)}}{{1 + \cos \left( {\frac{\pi }{2} – t} \right)}}} \right)( – dt)$ $= \int_0^{\pi /2} {\ln } \left( {\frac{{1 + \cos t}}{{1 + \sin t}}} \right)dt$ $= – \int_0^{\pi /2} {\ln } \left( {\frac{{1 + \sin t}}{{1 + \cos t}}} \right)dt.$

$= – \int_0^{\pi /2} {\ln } \left( {\frac{{1 + \sin x}}{{1 + \cos x}}} \right)dx = – I$ $\Leftrightarrow 2I = 0$ $\Leftrightarrow I = 0.$

Chú ý: Nếu ta phát biểu lại tính chất 6 dưới dạng: Giả sử $f(x)$ liên tục trên $\left[ {a;b} \right]$, khi đó: $\int_a^b f (x)dx = \int_b^a f (a + b – x)dx.$ Điều đó sẽ giúp chúng ta có được một phương pháp đổi biến mới, cụ thể ta xét ví dụ sau:

<!-- chunk:7 level:3 source:https://toanmath.com/2020/03/cac-tich-phan-dac-biet.html -->
## Ví dụ 7: Tính tích phân $I = \int_0^{\pi /4} {\ln } (1 + \tan x)dx.$

Lời giải:

Đặt $t = \frac{\pi }{4} – x$ $\Rightarrow dx = – dt.$

Đổi cận: $x = 0 \Rightarrow t = \frac{\pi }{4}$, $x = \frac{\pi }{4} \Rightarrow t = 0.$

Khi đó: $I = – \int_{\pi /4}^0 {\ln } \left[ {1 + \tan \left( {\frac{\pi }{4} – t} \right)} \right]dt$ $= \int_0^{\pi /4} {\ln } \left( {1 + \frac{{1 – \tan t}}{{1 + \tan t}}} \right)dt$ $= \int_0^{\pi /4} {\ln } \frac{2}{{1 + \tan t}}dt.$

$= \int_0^{\pi /4} {\left[ {\ln 2 – \ln (1 + \tan t)} \right]dt}$ $= \ln 2\int_0^{\pi /4} {dt} – \int_0^{\pi /4} {\ln } (1 + \tan t)dt$ $= \ln 2.\left. t \right|_0^{\pi /4} – I.$

$\Leftrightarrow 2I = \frac{{\pi \ln 2}}{4}$ $\Leftrightarrow I = \frac{{\pi \ln 2}}{8}.$

Tính chất 7: Nếu $f(x)$ liên tục trên đoạn $\left[ {0;2a} \right]$ với $a > 0$ thì: $\int_0^{2a} f (x)dx$ $= \int_0^a {\left[ {f(x) + f(2a – x)} \right]dx} .$

Chứng minh:

Ta có: $\int_0^{2a} f (x)dx$ $= \int_0^a f (x)dx + \int_a^{2a} f (x)dx$ $(1).$

Xét tích phân ${I_2} = \int_a^{2a} f (x)dx$ bằng cách đặt $x = 2a – t$ $\Rightarrow dx = – dt.$

Đổi cận: $x = a \Rightarrow t = a$, $x = 2a \Rightarrow t = 0.$

Khi đó: ${I_2} = – \int_a^0 f (2a – t)dt$ $= \int_0^a f (2a – t)dt$ $= \int_0^a f (2a – x)dx$ $(2).$

Thay $(2)$ vào $(1)$ ta được: $\int_0^{2a} f (x)dx$ $= \int_0^a f (x)dx + \int_0^a f (2a – x)dx$ $\int_0^a {\left[ {f(x) + f(2a – x)} \right]dx} .$

<!-- chunk:8 level:3 source:https://toanmath.com/2020/03/cac-tich-phan-dac-biet.html -->
## Ví dụ 8: Tính tích phân: $I = \int_0^{3\pi } {\sin x.\sin 2x.\sin 3x.\cos 5xdx} .$

Lời giải:

Viết lại $I$ dưới dạng:

$I = \int_0^{3\pi /2} {\sin x.\sin 2x.\sin 3x.\cos 5xdx}$ $+ \int_{3\pi /2}^{3\pi } {\sin x.\sin 2x.\sin 3x.\cos 5xdx}$ $(1).$

Xét tích phân $J = \int_{3\pi /2}^{3\pi } {\sin x.\sin 2x.\sin 3x.\cos 5xdx} .$

Đặt $x = 3\pi – t$ $\Rightarrow dx = – dt.$

Đổi cận: $x = \frac{{3\pi }}{2} \Rightarrow t = \frac{{3\pi }}{2}$, $x = 3\pi \Rightarrow t = 0.$

Khi đó: $J = – \int_{3\pi /2}^0 {\sin (3\pi – t).\sin 2(3\pi – t).\sin 3(3\pi – t).\cos 5(3\pi – t)dt} .$

$= – \int_0^{3\pi /2} {\sin t.\sin 2t.\sin 3t.\cos 5tdt} .$

$= – \int_0^{3\pi /2} {\sin x.\sin 2x.\sin 3x.\cos 5xdx}$ $(2).$

Thay $(2)$ vào $(1)$, ta được: $I = 0.$

Tính chất 8: Nếu $f(x)$ liên tục trên $R$ và tuần hoàn với chu kỳ $T$ thì $\int_a^{a + T} f (x)dx = \int_0^T f (x)dx.$

Chứng minh:

Ta có: $\int_0^T f (x)dx$ $= \int_0^a f (x)dx$ $+ \int_a^{a + T} f (x)dx$ $+ \int_{a + T}^T f (x)dx.$

Xét tích phân ${I_3} = \int_{a + T}^T f (x)dx$ bằng cách đặt $t = x – T$ $\Rightarrow dx = dt.$

Đổi cận: $x = a + T \Rightarrow t = a$, $x = T \Rightarrow t = 0.$

Khi đó: ${I_3} = \int_a^0 f (t + T)dt$ $= – \int_0^a f (t)dt = – \int_0^a f (x)dx$ $(2).$

Thay $(2)$ vào $(1)$ ta được:

$\int_0^T f (x)dx$ $= \int_a^{a + T} f (x)dx.$

<!-- chunk:9 level:3 source:https://toanmath.com/2020/03/cac-tich-phan-dac-biet.html -->
## Ví dụ 9: Tính tích phân: $I = \int_0^{2004\pi } {\sqrt {1 – \cos 2x} dx} .$

Lời giải:

Viết lại $I$ dưới dạng:

$I = \sqrt 2 \int_0^{2004\pi } {\left| {\sin x} \right|dx} .$

$= \sqrt 2 \left( {\int_0^{2\pi } {|\sin x|dx} + \int_{2\pi }^{4\pi } {|\sin x|dx} + \ldots + \int_{2002\pi }^{2004\pi } {|\sin x|dx} } \right)$ $(*).$

Theo tính chất 8, ta được:

$\int_0^{2\pi } {|\sin x|dx}$ $= \int_{2\pi }^{4\pi } {|\sin x|dx}$ $= \ldots = \int_{2002\pi }^{2004x} {|\sin x|dx} .$

Vậy: $(*) \Leftrightarrow I = 1002\sqrt 2 \int_0^{2\pi } {|\sin x|dx}$ $= 1002\left( {\int_0^{2\pi } {|\sin x|dx} – \int_0^\pi {\sin xdx} } \right).$

$= 1002\sqrt 2 \left( { – \left. {\cos x} \right|_0^\pi + \left. {\cos x} \right|_\pi ^{2\pi }} \right)$ $= 4008\sqrt 2 .$