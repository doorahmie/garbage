// Get the canvas element
const canvas = document.getElementById('sand');
const ctx = canvas.getContext('2d');

// Set the canvas dimensions
canvas.width = 300;
canvas.height = 300;

// Create the sand particles
for (let i = 0; i < 100; i++) {
  const x = Math.random() * canvas.width;
  const y = Math.random() * canvas.height;
  const size = Math.random() * 5 + 1;
  ctx.beginPath();
  ctx.arc(x, y, size, 0, 2 * Math.PI);
  ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
  ctx.fill();
}

// Animate the sand flowing
function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  for (let i = 0; i < 100; i++) {
    const particle = {
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      size: Math.random() * 5 + 1,
      speed: Math.random() * 2 + 1,
    };
    ctx.beginPath();
    ctx.arc(particle.x, particle.y, particle.size, 0, 2 * Math.PI);
    ctx.fillStyle = 'rgba(255, 255, 255, 0.5)';
    ctx.fill();
    particle.y += particle.speed;
    if (particle.y > canvas.height) {
      particle.y = 0;
      particle.x = Math.random() * canvas.width;
    }
  }
  requestAnimationFrame(animate);
}

animate();