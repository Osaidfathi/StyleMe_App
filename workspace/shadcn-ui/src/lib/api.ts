// API Configuration and Service Layer
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';

// API Response Types
export interface ApiResponse<T = any> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
}

export interface User {
  id: number;
  username: string;
  email: string;
  created_at?: string;
}

export interface AIAnalysisResult {
  analysis: {
    age: number;
    gender: Record<string, number>;
    race: Record<string, number>;
    emotion: Record<string, number>;
  };
  note?: string;
}

export interface HairstyleGenerationResult {
  generated_image: string;
  note?: string;
  prompt_used?: string;
}

export interface AIHealthStatus {
  status: string;
  deepface_available: boolean;
  hair_model_available: boolean;
  message: string;
}

// Generic API request function with error handling
async function apiRequest<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<ApiResponse<T>> {
  try {
    const url = `${API_BASE_URL}${endpoint}`;
    const response = await fetch(url, {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return {
      success: true,
      data,
    };
  } catch (error) {
    console.error(`API request failed for ${endpoint}:`, error);
    return {
      success: false,
      error: error instanceof Error ? error.message : 'Unknown error',
    };
  }
}

// User Management API
export const userApi = {
  // Get all users
  getUsers: (): Promise<ApiResponse<User[]>> => {
    return apiRequest<User[]>('/api/users');
  },

  // Create a new user
  createUser: (userData: { username: string; email: string }): Promise<ApiResponse<User>> => {
    return apiRequest<User>('/api/users', {
      method: 'POST',
      body: JSON.stringify(userData),
    });
  },

  // Delete a user
  deleteUser: (userId: number): Promise<ApiResponse<void>> => {
    return apiRequest<void>(`/api/users/${userId}`, {
      method: 'DELETE',
    });
  },

  // Update a user
  updateUser: (userId: number, userData: Partial<User>): Promise<ApiResponse<User>> => {
    return apiRequest<User>(`/api/users/${userId}`, {
      method: 'PUT',
      body: JSON.stringify(userData),
    });
  },
};

// AI Services API
export const aiApi = {
  // Check AI service health
  checkHealth: (): Promise<ApiResponse<AIHealthStatus>> => {
    return apiRequest<AIHealthStatus>('/api/ai/health');
  },

  // Analyze face from image
  analyzeFace: (imageData: string): Promise<ApiResponse<AIAnalysisResult>> => {
    return apiRequest<AIAnalysisResult>('/api/ai/analyze_face', {
      method: 'POST',
      body: JSON.stringify({ image: imageData }),
    });
  },

  // Generate hairstyle
  generateHairstyle: (imageData: string, prompt: string): Promise<ApiResponse<HairstyleGenerationResult>> => {
    return apiRequest<HairstyleGenerationResult>('/api/ai/generate_hairstyle', {
      method: 'POST',
      body: JSON.stringify({ image: imageData, prompt }),
    });
  },

  // Modify hairstyle
  modifyHairstyle: (imageData: string, modificationPrompt: string): Promise<ApiResponse<HairstyleGenerationResult>> => {
    return apiRequest<HairstyleGenerationResult>('/api/ai/modify_hairstyle', {
      method: 'POST',
      body: JSON.stringify({ image: imageData, modification_prompt: modificationPrompt }),
    });
  },
};

// Booking Management API (placeholder for future implementation)
export const bookingApi = {
  // Get all bookings
  getBookings: (): Promise<ApiResponse<any[]>> => {
    return apiRequest<any[]>('/api/booking/bookings');
  },

  // Create a new booking
  createBooking: (bookingData: any): Promise<ApiResponse<any>> => {
    return apiRequest<any>('/api/booking/bookings', {
      method: 'POST',
      body: JSON.stringify(bookingData),
    });
  },
};

// Salon Dashboard API (placeholder for future implementation)
export const salonApi = {
  // Get salon dashboard data
  getDashboardData: (): Promise<ApiResponse<any>> => {
    return apiRequest<any>('/api/salon/dashboard');
  },
};

// Admin Dashboard API (placeholder for future implementation)
export const adminApi = {
  // Get admin dashboard data
  getDashboardData: (): Promise<ApiResponse<any>> => {
    return apiRequest<any>('/api/admin/dashboard');
  },
};

// Utility functions
export const utils = {
  // Convert file to base64
  fileToBase64: (file: File): Promise<string> => {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => resolve(reader.result as string);
      reader.onerror = reject;
      reader.readAsDataURL(file);
    });
  },

  // Validate image file
  isValidImageFile: (file: File): boolean => {
    const validTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp'];
    const maxSize = 10 * 1024 * 1024; // 10MB
    
    return validTypes.includes(file.type) && file.size <= maxSize;
  },

  // Format error message
  formatErrorMessage: (error: string): string => {
    if (error.includes('Failed to fetch')) {
      return 'Unable to connect to server. Please check if the backend is running.';
    }
    if (error.includes('500')) {
      return 'Server error. Please try again later.';
    }
    if (error.includes('404')) {
      return 'Service not found. Please check the API endpoint.';
    }
    return error;
  },
};

export default {
  userApi,
  aiApi,
  bookingApi,
  salonApi,
  adminApi,
  utils,
};

