<template>
    <div class="col-12">
      <div class="card mt-4">
        <h5>API Data Table</h5>
        <DataTable
          :value="filteredData"
          :paginator="true"
          class="p-datatable-gridlines"
          :rows="10"
          dataKey="id"
          :rowHover="true"
          :loading="loadingApiData"
          responsiveLayout="scroll"
          :paginatorTemplate="customPaginatorTemplate"
        >
  
          <Column field="src" header="Source" :sortable="true"  />
          <Column field="dst" header="Destination" :sortable="true"  />
          <Column field="diversion" header="Diversion" :sortable="true" />
          <Column field="channel" header="Channel" :sortable="true" />
          <Column field="dst_channel" header="Destination Channel" :sortable="true" />
          <Column field="start" header="Start Time" :sortable="true" />
          <Column field="end" header="End Time" :sortable="true" />
          <Column field="duration" header="Duration" :sortable="true" />
          <Column field="disposition" header="Disposition" :sortable="true" />
          <Column field="pbx" header="PBX" :sortable="true" />
  
        </DataTable>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios';
  import { ref, onBeforeMount, computed } from 'vue';
  import { FilterMatchMode, FilterOperator } from 'primevue/api';
  
  const apiData = ref(null);
  const loadingApiData = ref(null);
  const filters = ref({ src: null, dst: null });
  
  onBeforeMount(async () => {
    // Загрузка данных из API
    try {
      const response = await axios.get('http://127.0.0.1:8000/api/get');
      apiData.value = response.data;
      loadingApiData.value = false;
    } catch (error) {
      console.error('Ошибка при загрузке данных из API', error);
      loadingApiData.value = false;
    }
  });
  
  const customPaginatorTemplate = {
    currentPageReport: '{currentPage} of {totalPages}',
    firstPageLink: '|<',
    lastPageLink: '>|',
    rowsPerPageDropdown: '10',
    prevPageLink: '<',
    nextPageLink: '>',
  };
  
  const filteredData = computed(() => {
  return apiData.value; // Отображаем все данные без фильтрации
});

  </script>
  
  <style scoped lang="scss">
  
  </style>
  