document.addEventListener('DOMContentLoaded', function() {
  const canvas = document.getElementById('taskChart');
  if (!canvas) return;

  const pending    = +canvas.dataset.pending    || 0;
  const inProgress = +canvas.dataset.inProgress || 0;
  const completed  = +canvas.dataset.completed  || 0;

  new Chart(canvas.getContext('2d'), {
    type: 'pie',
    data: {
      labels: ['Pending', 'In Progress', 'Completed'],
      datasets: [{
        data: [pending, inProgress, completed],
        backgroundColor: [
          '#F59E0B', // yellow
          '#3B82F6', // blue
          '#10B981'  // green
        ],
        borderColor: [
          '#D97706',
          '#1E40AF',
          '#047857'
        ],
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: 'bottom' },
        title: {
          display: true,
          text: 'Tasks by Status'
        }
      }
    }
  });
});
