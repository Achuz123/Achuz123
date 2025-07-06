🌟 Welcome to My Full-Stack Universe!

  Full-Stack Developer | Web & App Innovator



  B.Tech | Cyber Security & Digital Forensics | VIT Bhopal University
  Building dynamic, scalable web and mobile apps with a passion for secure, innovative solutions.
  Let's code the future together—full-stack style with a cybersecurity edge!





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



🛠️ My Full-Stack Toolkit

  
  
  
  
  
  
  
  
  
  
  
  
  



.skill-badge {
  transition: transform 0.4s ease, box-shadow 0.4s ease;
  border-radius: 8px;
}
.skill-badge:hover {
  transform: scale(1.15) rotate(3deg);
  box-shadow: 0 6px 12px rgba(0, 255, 136, 0.3);
}



📈 My GitHub Journey

  
  
  
  



.stats-card:hover {
  transform: scale(1.05);
}



🌍 Let's Connect!

  
    
  
  
    
  
  
    
  



.connect-badge {
  transition: transform 0.4s ease, box-shadow 0.4s ease;
  border-radius: 8px;
}
.connect-badge:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 12px rgba(0, 255, 136, 0.3);
}



✨ What's Next?

Diving deeper into full-stack development with a knack for secure systems. Got a project idea? Let's build it together!


document.addEventListener('DOMContentLoaded', () => {
  const badges = document.querySelectorAll('.skill-badge, .connect-badge, .stats-card');
  badges.forEach(badge => {
    badge.addEventListener('mouseover', () => {
      badge.style.cursor = 'pointer';
    });
  });
});
