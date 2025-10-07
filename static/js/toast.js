function showToast(title, message, type = 'normal', duration = 3000) {
  const toastComponent = document.getElementById('toast-component');
  const toastTitle = document.getElementById('toast-title');
  const toastMessage = document.getElementById('toast-message');
  const toastIcon = document.getElementById('toast-icon');

  if (!toastComponent) return;

  // Remove all type classes first
  toastComponent.classList.remove(
    'bg-[#ECFDF5]', 'bg-[#FEF2F2]', 'bg-[#FFFBEB]', 'bg-[#EFF6FF]',
    'text-[#14532D]', 'text-[#7F1D1D]', 'text-[#78350F]', 'text-[#1E3A8A]'
  );

  // Set type styles and icon
  if (type === 'success') {
    toastComponent.classList.add('bg-[#ECFDF5]', 'text-[#14532D]');
    toastComponent.style.border = '2px solid #16A34A';
    toastIcon.textContent = '✅';
  } else if (type === 'error') {
    toastComponent.classList.add('bg-[#FEF2F2]', 'text-[#7F1D1D]');
    toastComponent.style.border = '2px solid #DC2626';
    toastIcon.textContent = '❌';
  } else if (type === 'warning') {
    toastComponent.classList.add('bg-[#FFFBEB]', 'text-[#78350F]');
    toastComponent.style.border = '2px solid #F59E0B';
    toastIcon.textContent = '⚠️';
  } else {
    toastComponent.classList.add('bg-[#EFF6FF]', 'text-[#1E3A8A]');
    toastComponent.style.border = '2px solid #3B82F6';
    toastIcon.textContent = '';
  }

  // Update konten
  toastTitle.textContent = title;
  toastMessage.textContent = message;

  // Nampilin animasi
  toastComponent.classList.remove('opacity-0', 'translate-y-64');
  toastComponent.classList.add('opacity-100', 'translate-y-0');

  // Hilangin otomatis
  setTimeout(() => {
    toastComponent.classList.remove('opacity-100', 'translate-y-0');
    toastComponent.classList.add('opacity-0', 'translate-y-64');
  }, duration);
}
