<template>
    <div class="grid">
      <div class="col-12 lg:col-6 xl:col-3">
        <div class="card mb-0">
          <div class="flex justify-content-between mb-3">
            <div>
              <span class="block text-500 font-medium mb-3">All CDRs</span>
              <div class="text-900 font-medium text-xl">{{ cdrCount }}</div>
            </div>
            <!-- <div class="flex align-items-center justify-content-center bg-blue-100 border-round" style="width: 2.5rem; height: 2.5rem">
              <i class="pi pi-shopping-cart text-blue-500 text-xl"></i>
            </div> -->
          </div>
          <span class="text-green-500 font-medium">100 новых </span>
          <span class="text-500">с момента последнего посещения</span>
        </div>
      </div>
      <div class="col-12 lg:col-6 xl:col-3">
        <div class="card mb-0">
          <div class="flex justify-content-between mb-3">
            <div>
              <span class="block text-500 font-medium mb-3">All Users</span>
              <div class="text-900 font-medium text-xl">{{ cdrCount }}</div>
            </div>
            <!-- <div class="flex align-items-center justify-content-center bg-blue-100 border-round" style="width: 2.5rem; height: 2.5rem">
              <i class="pi pi-shopping-cart text-blue-500 text-xl"></i>
            </div> -->
          </div>
          <span class="text-green-500 font-medium">10 </span>
                <span class="text-500">newly registered</span>
        </div>
      </div>
      <div class="col-12 lg:col-6 xl:col-3">
        <div class="card mb-0">
          <div class="flex justify-content-between mb-3">
            <div>
              <span class="block text-500 font-medium mb-3">Free space disk</span>
              <div class="text-900 font-medium text-xl">{{ cdrCount }}</div>
            </div>
            <!-- <div class="flex align-items-center justify-content-center bg-blue-100 border-round" style="width: 2.5rem; height: 2.5rem">
              <i class="pi pi-shopping-cart text-blue-500 text-xl"></i>
            </div> -->
          </div>
          <span class="text-green-500 font-medium">-10 GB </span>
          <span class="text-500">from yesterday</span>
        </div>
      </div>
      <div class="col-12 lg:col-6 xl:col-3">
        <div class="card mb-0">
          <div class="flex justify-content-between mb-3">
            <div>
              <span class="block text-500 font-medium mb-3">Today traff</span>
              <div class="text-900 font-medium text-xl">{{ cdrCount }}</div>
            </div>
            <!-- <div class="flex align-items-center justify-content-center bg-blue-100 border-round" style="width: 2.5rem; height: 2.5rem">
              <i class="pi pi-shopping-cart text-blue-500 text-xl"></i>
            </div> -->
          </div>
          <span class="text-green-500 font-medium">%52+ </span>
                <span class="text-500">since last week</span>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios';
  import { onMounted, ref, reactive, watch } from 'vue';
  import ProductService from '@/service/ProductService';
  import { useLayout } from '@/layout/composables/layout';
  
  const { isDarkTheme } = useLayout();
  
  const cdrCount = ref(0);
  const products = ref(null);
  
  const lineOptions = ref(null);
  const productService = new ProductService();
  
  const items = ref([
    { label: 'Add New', icon: 'pi pi-fw pi-plus' },
    { label: 'Remove', icon: 'pi pi-fw pi-minus' }
    ]);
    
  onMounted(() => {
    productService.getProductsSmall().then((data) => (products.value = data));
    });

  const formatCurrency = (value) => {
    return value.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
  };
  
  const applyLightTheme = () => {
    lineOptions.value = {
      plugins: {
        legend: {
          labels: {
            color: '#495057',
          },
        },
      },
      scales: {
        x: {
          ticks: {
            color: '#495057',
          },
          grid: {
            color: '#ebedef',
          },
        },
        y: {
          ticks: {
            color: '#495057',
          },
          grid: {
            color: '#ebedef',
          },
        },
      },
    };
  };
  
  const applyDarkTheme = () => {
    lineOptions.value = {
      plugins: {
        legend: {
          labels: {
            color: '#ebedef',
          },
        },
      },
      scales: {
        x: {
          ticks: {
            color: '#ebedef',
          },
          grid: {
            color: 'rgba(160, 167, 181, .3)',
          },
        },
        y: {
          ticks: {
            color: '#ebedef',
          },
          grid: {
            color: 'rgba(160, 167, 181, .3)',
          },
        },
      },
    };
  };
  
  const updateCdrCount = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/get/');
      console.log(response)
      cdrCount.value = response.data.length;
      console.log(cdrCount.value)
    } catch (error) {
      console.error('Ошибка при получении CDR:', error);
    }
  };
  
  onMounted(() => {
    productService.getProductsSmall().then((data) => (products.value = data));
    updateCdrCount();
  });
  
  watch(
    isDarkTheme,
    (val) => {
      if (val) {
        applyDarkTheme();
      } else {
        applyLightTheme();
      }
    },
    { immediate: true }
  );
  </script>
  