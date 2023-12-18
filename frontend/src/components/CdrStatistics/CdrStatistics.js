import { VDataTable } from 'vuetify/lib/components/VDataTable';

export default {
  name: 'CdrStatisticsView',
  components: {
    VDataTable,
  },
  data() {
    return {
      cdrList: [],
      searchSRS: '',
      originalCdrList: [],
      isSearchActive: false,
      itemsPerPage: 10,
      totalItems: 0,
      pagination: {
        page: 1,
      },
      headers: [
        { text: 'ID', value: 'id' },
        { text: 'Source', value: 'src' },
        { text: 'Destination', value: 'dst' },
        { text: 'Start Time', value: 'start' },
        { text: 'Answer Time', value: 'answer' },
        { text: 'End Time', value: 'end' },
        { text: 'Duration (sec)', value: 'duration' },
        { text: 'Billable Seconds', value: 'billsec' },
        { text: 'Disposition', value: 'disposition' },
      ],
    };
  },
  created() {
    this.fetchCDRList();
    this.intervalId = setInterval(this.fetchCDRList, 10000);
  },
  unmounted() {
    clearInterval(this.intervalId);
  },
  methods: {
    async fetchCDRList() {
      try {
        const response = await this.$axios.get('http://127.0.0.1:8000/api/get/');
        if (response && response.data) {
          this.originalCdrList = response.data;
          this.totalItems = this.originalCdrList.length;

          // Применение фильтрации, если поиск активен
          if (this.isSearchActive) {
            this.filterData();
          } else {
            this.cdrList = this.originalCdrList;
          }
        } else {
          console.error('Invalid response format:', response);
        }
      } catch (error) {
        console.error('Error fetching CDR list:', error);
      }
    },
    updatePage(page) {
      this.pagination.page = page;
    },
    updateItemsPerPage(itemsPerPage) {
      this.itemsPerPage = itemsPerPage;
      this.pagination.page = 1; // Сбрасываем страницу при изменении количества элементов на странице
    },
  },
};
