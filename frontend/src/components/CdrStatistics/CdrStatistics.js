export default {
    name: 'CdrStatisticsView',
    data() {
      return {
        cdrList: [],
        itemsPerPage: 10, // Количество элементов на странице
        currentPage: 1,
      };
    },
    computed: {
      paginatedCdrList() {
        const startIndex = (this.currentPage - 1) * this.itemsPerPage;
        const endIndex = startIndex + this.itemsPerPage;
        return this.cdrList.slice(startIndex, endIndex);
      },
      totalPages() {
        return Math.ceil(this.cdrList.length / this.itemsPerPage);
      },
    },
    created() {
      this.fetchCDRList();
      // Загрузка данных каждые 10 секунд
      this.intervalId = setInterval(this.fetchCDRList, 5000);
    },
    unmounted() {
      // Очистка интервала при уничтожении компонента
      clearInterval(this.intervalId);
    },
    methods: {
      async fetchCDRList() {
        try {
          const response = await this.$axios.get('http://127.0.0.1:8000/api/get/');
          if (response && response.data) {
            this.cdrList = response.data;
  
            // Обновление currentPage при изменении данных
            if (this.currentPage > this.totalPages) {
              this.currentPage = this.totalPages;
            }
          } else {
            console.error('Invalid response format:', response);
          }
        } catch (error) {
          console.error('Error fetching CDR list:', error);
        }
      },
      refreshData() {
        // Метод для ручного обновления данных
        this.fetchCDRList();
      },
      changePage(offset) {
        this.currentPage += offset;
      },
    },
  };

  