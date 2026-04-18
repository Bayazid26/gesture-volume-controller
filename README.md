# ✋ Gesture Volume Controller (AI + Computer Vision)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv">
  <img src="https://img.shields.io/badge/MediaPipe-Hand%20Tracking-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
</p>

---

## 🖼️ Project Preview

<p align="center">
  <img src="https://i.ytimg.com/vi/9iEPzbG-xLE/hqdefault.jpg" width="600">
</p>

---

## 🚀 Overview

A real-time **AI-powered gesture control system** that lets you adjust your **system volume using hand movements** via webcam.

It uses computer vision + hand tracking to convert finger distance into smooth audio control.

---

## 🧠 Features

- ✋ Real-time hand tracking using MediaPipe  
- 🔊 System volume control via gestures  
- 🎯 Smooth volume transitions (no sudden jumps)  
- 📉 Noise reduction & stability filtering  
- ⚡ Lightweight & fast Python execution  
- 🧩 Modular clean architecture  

---

## 🧠 How It Works

```text
📷 Webcam Input
      ↓
🤖 MediaPipe Hand Detection
      ↓
📍 Extract Finger Landmarks
      ↓
📏 Calculate Distance (Thumb ↔ Index)
      ↓
🧠 Smooth Filtering
      ↓
🔊 Control System Volume (Pycaw)
