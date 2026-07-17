<div align="center">

<img src="resources/QTVdocs.png" alt="Q-TV" width="340">

<h3>Your apps. Your screen. Your way.</h3>

<p>
A modern TV interface for your PC. Q-TV brings a simple, remote-friendly<br>experience to your desktop with an app-first design.
</p>

</div>

# Contributing

Thank you for your interest in contributing to Q-TV! This guide explains how to set up the development environment and contribute to the project.

> [!TIP]
> New to open source? Take a moment to read the [Open Source Etiquette](https://developer.mozilla.org/en-US/docs/MDN/Community/Open_source_etiquette) guide first. It provides useful guidelines and practices to help you contribute effectively and respectfully.

> [!IMPORTANT]
> A basic understanding of Git and GitHub is expected. If these tools are still unfamiliar, check out [GitHub for complete beginners](https://github.com/git-guides#learning-git-basics) to learn the fundamentals before continuing.

> [!NOTE]
> Q-TV is currently under active development. Some features may change, break, or be redesigned in future updates.

<details>
<summary>English</summary>

## Prerequisites

| Component | Requirement      | Note                                                                                                                   |
| --------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Python    | 3.9+             | Developed and tested with Python 3.14                                                                                  |
| Git       | Latest version   | Required for cloning and contributing                                                                                  |
| Waydroid  | Android TV image | Required only for Android TV application integration. See the installation guide[here](https://github.com/WayDroid-ATV) |

## Getting Started

Clone the repository:

```bash
git clone https://github.com/nbao210/qtv-shell.git
cd qtv-shell
```

## Development Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

**Linux/macOS**:

```bash
source .venv/bin/activate
```

**Windows**:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Q-TV

Start the application:

```bash
python main.py
```

## Code Guidelines

1. Keep the existing project structure.
2. Use clear and descriptive names.
3. Keep changes focused on a single feature or fix.
4. Test your changes before submitting a pull request.

## Pull Requests

Before opening a pull request:

- Make sure the application runs correctly.
- Describe what changed and why.
- Include screenshots for UI changes when possible.

</details>

<details>
<summary>Tiếng Việt</summary>
<br>


> [!TIP]
> Contributor Việt Nam có thể sử dụng tiếng Việt khi trao đổi hoặc báo lỗi. Tiếng Anh được khuyến khích cho Pull Request và tài liệu công khai để việc cộng tác trở nên dễ dàng hơn với mọi người.


## Chuẩn Bị

| Thành phần | Yêu cầu              | Ghi chú                                                                                                                           |
| ------------ | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Python       | 3.9+                   | Được phát triển và kiểm thử với Python 3.14                                                                               |
| Git          | Phiên bản mới nhất | Cần thiết để clone và đóng góp                                                                                             |
| Waydroid     | Android TV image       | Chỉ bắt buộc khi tích hợp các ứng dụng Android TV. Xem hướng dẫn cài đặt[tại đây](https://github.com/WayDroid-ATV) |

## Thiết lập dự án

Clone repository:

```bash
git clone https://github.com/nbao210/qtv-shell.git
cd qtv-shell
```

## Thiết lập môi trường phát triển

Tạo môi trường ảo:

```bash
python -m venv .venv
```

Kích hoạt môi trường ảo:

**Đối với Linux/macOS**:

```bash
source .venv/bin/activate
```

**Đối với Windows**:

```bash
.venv\Scripts\activate
```

Cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

## Chạy Q-TV

Khởi động giao diện Shell Q-TV:

```bash
python main.py
```

## Quy tắc đóng góp code

1. Giữ nguyên cấu trúc hiện có của dự án.
2. Đặt tên rõ ràng, dễ hiểu cho biến, hàm và các thành phần trong code.
3. Mỗi thay đổi nên tập trung vào một tính năng hoặc một lỗi cụ thể.
4. Kiểm tra kỹ thay đổi trước khi gửi pull request.

## Pull Requests

Trước khi tạo pull request:

- Đảm bảo ứng dụng có thể chạy bình thường.
- Mô tả những thay đổi đã thực hiện và lý do thay đổi.
- Nếu có thay đổi về giao diện, hãy đính kèm ảnh chụp màn hình khi có thể.

</details>
