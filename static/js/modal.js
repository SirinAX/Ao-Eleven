// modal.js
document.addEventListener("DOMContentLoaded", () => {
  const csrftoken = document.cookie.split('; ').find(row => row.startsWith('csrftoken='))?.split('=')[1];
  const productList = document.getElementById("product-list");
  const refreshBtn = document.getElementById("refresh-products");

  // 🔹 State Visual
  function showLoadingState() {
    productList.innerHTML = `
      <div class="flex flex-col items-center justify-center w-full py-10 text-gray-500">
        <svg class="animate-spin h-8 w-8 text-blue-500 mb-3" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor"
                d="M4 12a8 8 0 018-8v4l3-3-3-3v4a8 8 0 100 16v-4l-3 3 3 3v-4a8 8 0 01-8-8z"></path>
        </svg>
        <p>Memuat produk...</p>
      </div>`;
  }

  function showEmptyState() {
    productList.innerHTML = `
      <div class="flex flex-col items-center justify-center w-full py-10 text-gray-500">
        <img src="/static/image/download.jpeg" alt="Empty" class="w-40 h-40 mb-3 object-contain">
        <p class="text-lg font-semibold">Belum ada produk 😔</p>
        <p class="text-sm text-gray-400">Tambahkan produk baru yuk!</p>
      </div>`;
  }

  function showErrorState() {
    productList.innerHTML = `
      <div class="flex flex-col items-center justify-center w-full py-10 text-red-600">
        <svg xmlns="http://www.w3.org/2000/svg" class="w-10 h-10 mb-3" fill="none" viewBox="0 0 24 24"
             stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
        </svg>
        <p class="font-semibold">Gagal memuat produk!</p>
        <p class="text-sm text-gray-500">Silakan coba lagi nanti.</p>
      </div>`;
  }

  // 🔹 Refresh Products
  async function refreshProducts() {
    const params = new URLSearchParams(window.location.search);
    const filter = params.get("filter") || "all";

    showLoadingState();
    try {
      const ajaxUrl = productList.dataset.ajaxUrl || "/products-list-ajax/";
      const res = await fetch(`${ajaxUrl}?filter=${filter}`);
      if (!res.ok) throw new Error("Gagal fetch");
      const data = await res.json();
      if (data.html && data.html.trim() !== "") {
        productList.innerHTML = data.html;
      } else {
        showEmptyState();
      }
    } catch (err) {
      console.error(err);
      showErrorState();
    }
  }

  refreshBtn?.addEventListener("click", refreshProducts);

  // 🔹 Modal Show/Hide
  function showModal(isEdit=false, product=null){
    const modal = document.getElementById("crudModal");
    const content = document.getElementById("crudModalContent");
    const form = document.getElementById("productForm");

    if(!isEdit) form.reset();
    document.getElementById("product-id").value = "";

    if(isEdit && product){
      document.getElementById("crudModalTitle").textContent = "Edit Product";
      document.getElementById("crudModalSubtitle").textContent = "Update product info";
      document.getElementById("product-id").value = product.id;

      const fields = {
        "id_name": product.name,
        "id_price": product.price,
        "id_stock": product.stock,
        "id_description": product.description,
        "id_category": product.category,
        "id_thumbnail": product.thumbnail,
        "id_brand": product.brand,
        "id_rating": product.rating,
        "id_is_featured": product.is_featured
      };
      for(const id in fields){
        const el = document.getElementById(id);
        if(el){
          if(el.type === "checkbox") el.checked = fields[id] === true || fields[id] === "true";
          else el.value = fields[id];
        }
      }
    }

    modal.classList.remove("hidden");
    content.classList.remove("opacity-0","scale-95");
    content.classList.add("opacity-100","scale-100");
  }

  function hideModal(){
    const modal = document.getElementById("crudModal");
    const content = document.getElementById("crudModalContent");
    content.classList.remove("opacity-100","scale-100");
    content.classList.add("opacity-0","scale-95");
    setTimeout(()=> modal.classList.add("hidden"), 200);
  }

  window.showModal = showModal;
  window.hideModal = hideModal;

  // 🔹 Delete modal
  let deleteId = null;
  function showDeleteModal(id){ deleteId=id; document.getElementById("deleteModal").classList.remove("hidden"); }
  function hideDeleteModal(){ deleteId=null; document.getElementById("deleteModal").classList.add("hidden"); }

  window.showDeleteModal = showDeleteModal;
  window.hideDeleteModal = hideDeleteModal;

  document.getElementById("confirmDeleteBtn")?.addEventListener("click", async ()=>{
    if(!deleteId) return;
    try{
      const res = await fetch(`/delete-product/${deleteId}/`, {
        method: "POST",
        headers: {"X-Requested-With":"XMLHttpRequest","X-CSRFToken":csrftoken}
      });
      const data = await res.json();
      if(data.success){
        document.getElementById(`product-${deleteId}`)?.remove();
        showToast("Product deleted!","success");
        if(!productList.querySelector(".product-card")) showEmptyState();
      } else {
        showToast("Failed to delete product","error");
      }
    }catch(err){
      console.error(err);
      showToast("Error deleting product","error");
    }
    hideDeleteModal();
  });

  // 🔹 AJAX Add/Edit Product
  document.getElementById("productForm")?.addEventListener("submit", async function(e){
    e.preventDefault();
    const formData = new FormData(this);
    const productId = formData.get("id");
    const url = productId ? `/edit-product-ajax/${productId}/` : "/create-product-ajax/";

    try{
      const res = await fetch(url,{
        method:"POST",
        body: formData,
        headers: {"X-Requested-With":"XMLHttpRequest","X-CSRFToken":csrftoken}
      });
      const data = await res.json();
      if(data.success){
        if(productId){
          const card = document.getElementById(`product-${productId}`);
          if(card) card.outerHTML = data.html;
        } else {
          if(productList.querySelector(".flex.flex-col.items-center")) productList.innerHTML = data.html;
          else productList.insertAdjacentHTML("beforeend", data.html);
        }
        hideModal();
        showToast(productId ? "Product updated!" : "Product added!","success");
      } else {
        showToast("Failed! "+(data.error||""),"error");
      }
    }catch(err){
      console.error(err);
      showToast("Error submitting product","error");
    }
    // cek empty state kalau semua dihapus
    if(!productList.querySelector(".product-card")) showEmptyState();
  });

  // 🔹 Initial load empty check
  if(!productList.querySelector(".product-card")) showEmptyState();
});
