# 🌟 Welcome to My Full-Stack Universe!

<div align="center" style="min-height: 40px; font-size: 1.5rem; font-family: 'Fira Code', monospace; color: #00FF88;">
  <span class="glitch" data-text="Full-Stack Developer | Web & App Innovator">Full-Stack Developer | Web & App Innovator</span>
</div>

<p align="center">
  B.Tech | Cyber Security & Digital Forensics | VIT Bhopal University<br>
  Building dynamic, scalable web and mobile apps with a passion for secure, innovative solutions.<br>
  Let's code the future together—full-stack style with a cybersecurity edge!
</p>

<!-- Particle Background -->
<canvas id="particle-canvas" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1; opacity: 0.2;"></canvas>

<style>
.glitch {
  position: relative;
  color: #00FF88;
  animation: glitch 1s linear infinite;
}
.glitch::before, .glitch::after {
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  color: #00FF88;
}
.glitch::before {
  left: 2px;
  text-shadow: -2px 0 #ff00c1;
  animation: glitch-top 1s linear infinite;
  clip-path: polygon(0 0, 100% 0, 100% 33%, 0 33%);
}
.glitch::after {
  left: -2px;
  text-shadow: 2px 0 #00fff9;
  animation: glitch-bottom 1.5s linear infinite;
  clip-path: polygon(0 67%, 100% 67%, 100% 100%, 0 100%);
}
@keyframes glitch {
  2%, 64% { transform: translate(2px, 0) skew(0deg); }
  4%, 60% { transform: translate(-2px, 0) skew(0deg); }
  62% { transform: translate(0, 0) skew(5deg); }
}
@keyframes glitch-top {
  2%, 64% { transform: translate(2px, -2px); }
  4%, 60% { transform: translate(-2px, 2px); }
  62% { transform: translate(0, 0) skew(5deg); }
}
@keyframes glitch-bottom {
  2%, 64% { transform: translate(-2px, 0); }
  4%, 60% { transform: translate(2px, 0); }
  62% { transform: translate(0, 0) skew(5deg); }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', () => {
  // Particle Background
  const canvas = document.getElementById('particle-canvas');
  const ctx = canvas.getContext('2d');
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  const particlesArray = [];
  const numberOfParticles = 50;

  class Particle {
    constructor() {
      this.x = Math.random() * canvas.width;
      this.y = Math.random() * canvas.height;
      this.size = Math.random() * 5 + 1;
      this.speedX = Math.random() * 3 - 1.5;
      this.speedY = Math.random() * 3 - 1.5;
      this.opacity = Math.random() * 0.5 + 0.1;
    }
    update() {
      this.x += this.speedX;
      this.y += this.speedY;
      if (this.size > 0.2) this.size -= 0.05;
      if (this.opacity > 0) this.opacity -= 0.005;
    }
    draw() {
      ctx.fillStyle = `rgba(0, 255, 136, ${this.opacity})`;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  function init() {
    for (let i = 0; i < numberOfParticles; i++) {
      particlesArray.push(new Particle());
    }
  }

  function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let i = 0; i < particlesArray.length; i++) {
      particlesArray[i].update();
      particlesArray[i].draw();
      if (particlesArray[i].size <= 0.2 || particlesArray[i].opacity <= 0) {
        particlesArray.splice(i, 1);
        particlesArray.push(new Particle());
        i--;
      }
    }
    requestAnimationFrame(animate);
  }

  init();
  animate();
});
</script>

---

## 🛠️ My Full-Stack Toolkit

<div align="center" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 12px; padding: 20px;">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=000" class="skill-badge">
  <img src="https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=white" class="skill-badge">
  <img src="https://img.shields.io/badge/Node.js-6DA55F?logo=node.js&logoColor=white" class="skill-badge">
  <img src="https://img.shields.io/badge/Express.js-silver?logo=express&logoColor=black" class="skill-badge">
  <img src="https://img.shields.io/badge/MongoDB-green?logo=mongodb&logoColor=white" class="skill-badge">
  <img src="https://img.shields.io/badge/Tailwind%20CSS-blue?logo=tailwindcss&logoColor=white" class="skill-badge">
  <img src="https://img.shields.io/badge/Flutter-02569B?logo=flutter&logoColor=fff" class="skill-badge">
  <img src="https://img.shields.io/badge/Kotlin-%237F52FF.svg?logo=kotlin&logoColor=white" class="skill-badge">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff" class="skill-badge">
  <img src="https://img.shields.io/badge/Java-%23ED8B00.svg?logo=openjdk&logoColor=white" class="skill-badge">
  <img src="https://img.shields.io/badge/C++-%2300599C.svg?logo=c%2B%2B&logoColor=white" class="skill-badge">
  <img src="https://img.shields.io/badge/AWS-%23FF9900.svg?logo=amazon-web-services&logoColor=white" class="skill-badge">
  <img src="https://img.shields.io/badge/Firebase-039BE5?logo=Firebase&logoColor=white" class="skill-badge">
</div>

<style>
.skill-badge {
  transition: transform 0.4s ease, box-shadow 0.4s ease;
  border-radius: 8px;
}
.skill-badge:hover {
  transform: scale(1.15) rotate(3deg);
  box-shadow: 0 6px 12px rgba(0, 255, 136, 0.3);
}
</style>

---

## 📈 My GitHub Journey

<div align="center" style="display: flex; flex-wrap: wrap; justify-content: center; gap: 20px; padding: 20px;">
  <img src="https://github-readme-stats.vercel.app/api?username=achuz123&show_icons=true&theme=radical&hide_border=true&count_private=true" alt="GitHub Stats" style="max-width: 100%; transform: scale(1); transition: transform 0.3s ease;" class="stats-card">
  <img src="https://github-readme-stats.vercel.app/api/top-langs?username=achuz123&show_icons=true&locale=en&layout=compact&theme=radical&hide_border=true" alt="Top Languages" style="max-width: 100%; transform: scale(1); transition: transform 0.3s ease;" class="stats-card">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=achuz123&theme=radical&hide_border=true" alt="GitHub Streak" style="max-width: 100%; transform: scale(1); transition: transform 0.3s ease;" class="stats-card">
  <img src="https://github-profile-trophy.vercel.app/?username=achuz123&theme=onedark&no-frame=true&margin-w=10&column=3" alt="Trophies" style="max-width: 100%; transform: scale(1); transition: transform 0.3s ease;" class="stats-card">
</div>

<style>
.stats-card:hover {
  transform: scale(1.05);
}
</style>

---

## 🌍 Let's Connect!

<div align="center" style="display: flex; justify-content: center; gap: 15px; padding: 20px;">
  <a href="https://www.linkedin.com/in/achuth-b-424328251/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" class="connect-badge">
  </a>
  <a href="https://github.com/Achuz123" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" class="connect-badge">
  </a>
  <a href="mailto:achuthampi19@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" class="connect-badge">
  </a>
</div>

<style>
.connect-badge {
  transition: transform 0.4s ease, box-shadow 0.4s ease;
  border-radius: 8px;
}
.connect-badge:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 255, 136, 0.3);
}
</style>

---

## ✨ What's Next?

> Diving deeper into full-stack development with a knack for secure systems. Got a project idea? Let's build it together!

<script>
document.addEventListener('DOMContentLoaded', () => {
  const badges = document.querySelectorAll('.skill-badge, .connect-badge, .stats-card');
  badges.forEach(badge => {
    badge.addEventListener('mouseover', () => {
      badge.style.cursor = 'pointer';
    });
  });
});
</script>
