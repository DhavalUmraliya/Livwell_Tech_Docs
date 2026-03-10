# Insurance Dashboard Activity - API Documentation

## Screen Flow

### 1. Insurance Dashboard Activity

**Screen Purpose**: Main dashboard screen for insurance features. Displays available insurance types, user's insurance history, banners, testimonials, and allows users to browse and purchase insurance.

**Entry Point**: 
- Accessed from Dashboard Home Screen by clicking insurance icon/action

**User Actions Available**:
- View available insurance types/categories
- Select insurance type to purchase
- View insurance history/policies
- View insurance banners
- View testimonials/reviews
- Restart insurance purchase journey
- Navigate to wallet (view LWC balance)
- Navigate to My Policies
- Navigate to Vault
- Navigate to Employee Benefits
- Call support
- Chat support (Messenger/Intercom)
- Resume incomplete insurance purchase

---

## Test Cases / Unit Cases / Edge Cases

### Edge Case 1: No Insurance Categories

**Screen**: Insurance Dashboard Activity

**Scenario**: API returns empty `categorylist` array

**Test Case**:
- **Given**: No insurance categories available
- **When**: API returns empty category list
- **Then**: 
  - Insurance list section hidden
  - "Get Insured" title hidden
  - Other sections (banners, testimonials) still displayed if available

**Expected Behavior**: Insurance list section hidden, other content still visible

---

### Edge Case 2: No Insurance History

**Screen**: Insurance Dashboard Activity

**Scenario**: User has no insurance purchase history

**Test Case**:
- **Given**: User has never purchased insurance
- **When**: API returns empty `historyList` array
- **Then**: 
  - "My Policies" section hidden
  - Insurance list and other sections still displayed

**Expected Behavior**: My Policies section hidden

---

### Edge Case 3: Network Error

**Screen**: Insurance Dashboard Activity

**Scenario**: No internet connection or network timeout during API call

**Test Case**:
- **Given**: User has no internet connection
- **When**: API is called
- **Then**: 
  - Show error state with error message
  - Display retry option
  - User can retry when connection restored

**Expected Behavior**: Error state displayed with retry option

---

### Edge Case 4: Server Error (500+)

**Screen**: Insurance Dashboard Activity

**Scenario**: Server returns 500 or other server-side error

**Test Case**:
- **Given**: Server is experiencing issues
- **When**: API is called
- **Then**: 
  - Show error state with error message
  - Display retry option
  - User can retry later

**Expected Behavior**: Error state displayed with retry option

---

### Edge Case 5: Empty Banners List

**Screen**: Insurance Dashboard Activity

**Scenario**: API returns empty `banners` array

**Test Case**:
- **Given**: No banners available
- **When**: API returns empty banners list
- **Then**: 
  - Banners section not displayed
  - Other sections still displayed

**Expected Behavior**: Banners section hidden

---

### Edge Case 6: Empty Testimonials List

**Screen**: Insurance Dashboard Activity

**Scenario**: API returns empty `testimonialList` array

**Test Case**:
- **Given**: No testimonials available
- **When**: API returns empty testimonials list
- **Then**: 
  - Testimonials section hidden
  - Other sections still displayed

**Expected Behavior**: Testimonials section hidden

---

### Edge Case 7: External Insurance Resource Type

**Screen**: Insurance Dashboard Activity

**Scenario**: User selects insurance with `resourceType = "EXTERNAL"`

**Test Case**:
- **Given**: Insurance item has external resource type
- **When**: User clicks on insurance item
- **Then**: 
  - Navigate to Insurance Lead Generation Activity with URL
  - Internal purchase flow not initiated

**Expected Behavior**: External URL opened in lead generation screen

---

### Edge Case 8: Resume Insurance Purchase Journey

**Screen**: Insurance Dashboard Activity

**Scenario**: User has incomplete insurance purchase and selects same insurance

**Test Case**:
- **Given**: User has incomplete purchase for an insurance type
- **When**: User selects the same insurance type
- **Then**: 
  - Check if `canResumeJourney = true`
  - Show resume purchase popup with continue/restart options
  - User can continue from where left off or restart

**Expected Behavior**: Resume popup shown with options

---

### Edge Case 9: Restart Insurance Purchase Journey Failure

**Screen**: Insurance Dashboard Activity

**Scenario**: Restart journey API fails

**Test Case**:
- **Given**: User chooses to restart purchase journey
- **When**: Restart API call fails
- **Then**: 
  - Error message shown
  - User remains on screen
  - Can retry restart

**Expected Behavior**: Error displayed, user can retry

---

### Edge Case 10: Insurance Purchase Cancelled

**Screen**: Insurance Dashboard Activity

**Scenario**: User cancels insurance purchase and returns to dashboard

**Test Case**:
- **Given**: User navigates to purchase screen and cancels
- **When**: User returns to dashboard with cancelled result
- **Then**: 
  - Insurance list refreshed
  - Shimmer effect shown during refresh
  - Updated data displayed

**Expected Behavior**: List refreshed, updated data shown

---

### Edge Case 11: Insurance Purchase Completed

**Screen**: Insurance Dashboard Activity

**Scenario**: User completes insurance purchase and returns to dashboard

**Test Case**:
- **Given**: User completes insurance purchase
- **When**: User returns to dashboard with success result
- **Then**: 
  - Activity finishes
  - User returns to previous screen

**Expected Behavior**: Activity closed, user returns to previous screen

---

### Edge Case 12: Phone Permission Denied

**Screen**: Insurance Dashboard Activity

**Scenario**: User clicks "Call Now" but phone permission is denied

**Test Case**:
- **Given**: Phone permission not granted
- **When**: User clicks "Call Now" button
- **Then**: 
  - Permission request shown
  - If denied, call cannot be made
  - User can grant permission in settings

**Expected Behavior**: Permission handled gracefully

---

### Edge Case 13: No Resume Purchase Data

**Screen**: Insurance Dashboard Activity

**Scenario**: API returns `canResumeJourney = false` for insurance

**Test Case**:
- **Given**: No incomplete purchase journey
- **When**: User selects insurance
- **Then**: 
  - No resume popup shown
  - Directly navigate to purchase flow

**Expected Behavior**: Direct navigation to purchase flow

---

### Edge Case 14: Cardio Insurance Selection

**Screen**: Insurance Dashboard Activity

**Scenario**: User selects Cardio Insurance type

**Test Case**:
- **Given**: User selects Cardio Insurance
- **When**: Purchase journey starts
- **Then**: 
  - Navigate to Cardio Insurance Details Activity
  - Skip profile confirmation (uses EKYC journey)
  - Different flow than other insurance types

**Expected Behavior**: Cardio-specific purchase flow initiated

---

### Edge Case 15: First Insurance Auto-Selected

**Screen**: Insurance Dashboard Activity

**Scenario**: First insurance in list is auto-selected

**Test Case**:
- **Given**: Insurance list loaded
- **When**: List has items
- **Then**: 
  - First insurance item's `isSelected = true`
  - Visual indication of selection shown

**Expected Behavior**: First item visually selected

---

### Unit Test Case 1: Insurance List Filtering

**Test Case**:
- **Given**: Insurance list with multiple items
- **When**: List is displayed
- **Then**: All items shown in grid layout
- **Assert**: All items displayed correctly

---

### Unit Test Case 2: Resume Journey Check

**Test Case**:
- **Given**: Insurance with `canResumeJourney = true`
- **When**: User selects insurance
- **Then**: Resume popup shown
- **Assert**: Popup displayed with correct data

---

### Unit Test Case 3: External Resource Handling

**Test Case**:
- **Given**: Insurance with `resourceType = "EXTERNAL"`
- **When**: User selects insurance
- **Then**: Lead generation screen opened with URL
- **Assert**: External flow initiated

---

### Unit Test Case 4: History List Display

**Test Case**:
- **Given**: User has insurance history
- **When**: History list is not empty
- **Then**: "My Policies" section visible
- **Assert**: Section visibility matches history availability

---

### Unit Test Case 5: Banner Display

**Test Case**:
- **Given**: Banners list available
- **When**: Banners loaded
- **Then**: Banners displayed in horizontal scrollable list
- **Assert**: Banners shown with pagination

---

### Unit Test Case 6: Testimonials Display

**Test Case**:
- **Given**: Testimonials list available
- **When**: Testimonials loaded
- **Then**: Testimonials displayed in horizontal scrollable list
- **Assert**: Testimonials shown with pagination indicators

---

## API Flow

### Flow 1: Get Insurance List

**Screen**: Insurance Dashboard Activity  
**Trigger**: Screen loads automatically (API called in `onCreate`)

**Criteria**: 
- User must be logged in
- No additional parameters required

**API Name**: `GET /v4/insurance`

**Request Parameters**: None (uses authenticated user session)

**Request Format**:
- Method: GET
- Authentication: Required (Bearer Token)

**Response Structure**:
```json
{
  "statusCode": 200,
  "data": {
    "categorylist": [
      {
        "_id": "category_id",
        "logo": "https://...",
        "image": "https://...",
        "subName": "Sub Name",
        "name": "Insurance Name",
        "type": "BIKE_INSURANCE",
        "price": "From $X",
        "insuranceId": "insurance_id",
        "packageId": "package_id",
        "categoryId": "category_id",
        "packageValueAmount": 1000000,
        "isSelected": false,
        "hasAgeLimit": false,
        "ageLimit": {
          "min": 18,
          "max": 65
        },
        "isNewInsurance": false,
        "resumeInsurancePurchase": {
          "resumeScreenDeepLink": "/insurance/...",
          "canResumeJourney": false,
          "resumeTitle": "Continue Purchase",
          "resumeLogo": "https://...",
          "resumeDescription": "Continue your purchase",
          "categoryId": "category_id",
          "insuranceType": "BIKE_INSURANCE"
        },
        "message": "Message",
        "resourceType": "INTERNAL",
        "url": ""
      }
    ],
    "historyList": [
      {
        "_id": "history_id",
        "Policy": "POL123456",
        "insurancePurchaseId": "purchase_id",
        "type": "PERSONAL_LIFE_STYLE_INSURANCE",
        "insuranceType": "Personal Life Style",
        "policyStatus": "POLICY_ACTIVE",
        "insuranceId": "insurance_id",
        "insuranceCoverPage": "https://...",
        "insuranceName": "Insurance Name",
        "packageValue": 1000000,
        "premium": 50000,
        "premiumTerm": "Monthly",
        "endTime": "2024-12-31T00:00:00Z",
        "startTime": "2024-01-01T00:00:00Z",
        "PremiumTerm": 12
      }
    ],
    "testimonialList": [
      {
        "name": "John Doe",
        "image": "https://...",
        "testimonial": "Great service!"
      }
    ],
    "banners": [
      {
        "id": "banner_id",
        "image": "https://...",
        "linkType": "INTERNAL",
        "bannerLink": "/insurance/..."
      }
    ],
    "resumeInsurancePurchase": {
      "resumeScreenDeepLink": "/insurance/...",
      "canResumeJourney": true,
      "resumeTitle": "Continue Purchase",
      "resumeLogo": "https://...",
      "resumeDescription": "Continue your purchase",
      "categoryId": "category_id",
      "insuranceType": "BIKE_INSURANCE"
    }
  }
}
```

**Response Keys Usage**:

**Top Level**:
- `statusCode` (Integer):
  - `200` → Success: Process and display data
  - Other codes → Error: Show error state with retry option
- `data` (Object): Main data object

**Insurance Categories** (`data.categorylist`):
- Array of available insurance types
- Each category contains:
  - `_id` (String): Category ID
  - `logo` (String): Insurance logo URL
  - `image` (String): Insurance image URL
  - `name` (String): Insurance name displayed
  - `subName` (String): Insurance subtitle
  - `type` (String): Insurance type enum
  - `price` (String): Price display text (e.g., "From $X")
  - `categoryId` (String): Used for purchase journey
  - `packageValueAmount` (Long): Package value
  - `hasAgeLimit` (Boolean): Whether age limit applies
  - `ageLimit` (Object): Age limit range
  - `resumeInsurancePurchase` (Object): Resume purchase data for this category
  - `resourceType` (String): "INTERNAL" or "EXTERNAL"
  - `url` (String): External URL if resourceType is "EXTERNAL"
- Displayed in grid layout (3 columns)
- First item auto-selected (`isSelected = true`)

**Insurance History** (`data.historyList`):
- Array of user's purchased insurance policies
- Each history item contains:
  - `_id` (String): History ID
  - `Policy` (String): Policy number
  - `insuranceName` (String): Insurance name
  - `policyStatus` (String): Policy status
  - `premium` (Long): Premium amount
  - `packageValue` (Long): Coverage amount
  - `startTime` (String): Policy start date
  - `endTime` (String): Policy end date
- Used to show/hide "My Policies" section
- If empty → "My Policies" section hidden

**Testimonials** (`data.testimonialList`):
- Array of customer testimonials/reviews
- Each testimonial contains:
  - `name` (String): Reviewer name
  - `image` (String): Reviewer image URL
  - `testimonial` (String): Review text
- Displayed in horizontal scrollable list with pagination
- If empty → Testimonials section hidden

**Banners** (`data.banners`):
- Array of insurance banners
- Each banner contains:
  - `id` (String): Banner ID
  - `image` (String): Banner image URL
  - `linkType` (String): "INTERNAL", "EXTERNAL", or "NA"
  - `bannerLink` (String): Navigation URL
- Displayed in horizontal scrollable list with pagination
- If empty → Banners section hidden

**Resume Insurance Purchase** (`data.resumeInsurancePurchase`):
- Global resume purchase data (not category-specific)
- Contains:
  - `canResumeJourney` (Boolean): Whether user can resume purchase
  - `resumeScreenDeepLink` (String): Deep link to resume screen
  - `resumeTitle` (String): Resume card title
  - `resumeLogo` (String): Resume card logo
  - `resumeDescription` (String): Resume card description
  - `categoryId` (String): Category ID for resume
  - `insuranceType` (String): Insurance type for resume
- Used to show resume purchase card if available

**Success Flow**:
1. Display loading state (shimmer effect)
2. API call completes
3. Process response:
   - Extract insurance categories list
   - Extract insurance history list
   - Extract testimonials list
   - Extract banners list
   - Extract resume purchase data
4. Display:
   - Insurance categories in grid (3 columns)
   - First category auto-selected
   - "My Policies" section (if history available)
   - Banners (if available)
   - Testimonials (if available)
   - Resume purchase card (if `canResumeJourney = true`)

**Error Flow**:
- Show error state with error message
- Display retry option
- User can retry API call

---

### Flow 2: Restart Insurance Purchase Journey

**Screen**: Insurance Dashboard Activity  
**Trigger**: User selects "Restart" option in resume purchase popup

**Criteria**: 
- User has incomplete insurance purchase
- Valid `categoryId` available

**API Name**: `PUT /v3/insurance/purchase/restart`

**Request Parameters**:
| Parameter | Key | Type | Required | Source |
|-----------|-----|------|----------|--------|
| Category ID | `categoryId` | String | Yes | From selected insurance category |

**Request Format**:
- Method: PUT
- Content-Type: `application/x-www-form-urlencoded`
- Field Name: `data` (encrypted JSON string)
- Encryption: Parameters encrypted using AES before sending
- Request Body: Encrypted JSON containing:
  ```json
  {
    "categoryId": "category_id"
  }
  ```

**Response Structure**:
```json
{
  "statusCode": 200,
  "message": "Journey restarted successfully",
  "type": "SUCCESS"
}
```

**Response Keys Usage**:
- `statusCode` (Integer):
  - `200` → Success: Clear resume purchase data, navigate to purchase flow
  - Other codes → Error: Show error message
- `message` (String): Success/error message
- `type` (String): Response type

**Success Flow**:
1. Show loading indicator
2. Build request payload with `categoryId`
3. Encrypt payload using AES
4. API call with encrypted payload
5. On success:
   - Clear saved resume purchase data
   - Navigate to insurance purchase flow
   - If Cardio Insurance → Navigate to Cardio Insurance Details Activity
   - If other insurance → Navigate to Insurance Profile Confirmation Activity
6. Hide loading indicator

**Error Flow**:
- Hide loading indicator
- Show error message
- User remains on screen
- Can retry

**Cancel Flow**:
- If `cancelPurchaseJourney = true`:
  - Clear resume purchase data
  - Refresh insurance list
  - Resume purchase card hidden

---

## Summary Table

| Screen | Action | API | Params | Success Response Key Usage | Error Handling |
|--------|--------|-----|--------|---------------------------|----------------|
| Insurance Dashboard Activity | Load Insurance List | `GET /v4/insurance` | None | `data.categorylist` → Display insurance grid, `data.historyList` → Show/hide My Policies, `data.banners` → Display banners, `data.testimonialList` → Display testimonials, `data.resumeInsurancePurchase` → Show resume card | Show error state with retry |
| Insurance Dashboard Activity | Restart Purchase Journey | `PUT /v3/insurance/purchase/restart` | `categoryId` | `statusCode=200` → Clear resume data, navigate to purchase flow | Show error, allow retry |

---

## Response Model Details

### Insurance List Response Structure

**Main Response Object**:
- `statusCode` (Integer): HTTP status code
- `data` (Object): Main data object

**Insurance Category Object**:
- `_id` (String): Category ID
- `logo` (String): Logo URL
- `image` (String): Image URL
- `name` (String): Insurance name
- `subName` (String): Subtitle
- `type` (String): Insurance type enum
- `price` (String): Price display text
- `insuranceId` (String): Insurance ID
- `packageId` (String): Package ID
- `categoryId` (String): Category ID
- `packageValueAmount` (Long): Package value
- `isSelected` (Boolean): Selection state
- `hasAgeLimit` (Boolean): Age limit flag
- `ageLimit` (Object): Age limit range
- `isNewInsurance` (Boolean): New insurance flag
- `resumeInsurancePurchase` (Object): Resume purchase data
- `message` (String): Message
- `resourceType` (String): "INTERNAL" or "EXTERNAL"
- `url` (String): External URL

**Insurance History Object**:
- `_id` (String): History ID
- `Policy` (String): Policy number
- `insurancePurchaseId` (String): Purchase ID
- `type` (String): Insurance type
- `insuranceType` (String): Insurance type name
- `policyStatus` (String): Policy status
- `insuranceId` (String): Insurance ID
- `insuranceCoverPage` (String): Cover page URL
- `insuranceName` (String): Insurance name
- `packageValue` (Long): Coverage amount
- `premium` (Long): Premium amount
- `premiumTerm` (String): Premium term
- `endTime` (String): End date
- `startTime` (String): Start date
- `PremiumTerm` (Integer): Duration in months

**Testimonial Object**:
- `name` (String): Reviewer name
- `image` (String): Reviewer image URL
- `testimonial` (String): Review text

**Banner Object**:
- `id` (String): Banner ID
- `image` (String): Banner image URL
- `linkType` (String): Link type
- `bannerLink` (String): Navigation URL

**Resume Insurance Purchase Object**:
- `resumeScreenDeepLink` (String): Deep link to resume screen
- `canResumeJourney` (Boolean): Can resume flag
- `resumeTitle` (String): Resume card title
- `resumeLogo` (String): Resume card logo
- `resumeDescription` (String): Resume card description
- `categoryId` (String): Category ID
- `insuranceType` (String): Insurance type

### Restart Journey Response Structure

**Main Response Object**:
- `statusCode` (Integer): HTTP status code
- `message` (String): Response message
- `type` (String): Response type

---

## Navigation Flow

**Entry Point**: 
- From Dashboard Home Screen → Click Insurance Icon/Action → Insurance Dashboard Activity

```
Insurance Dashboard Activity
    ├── Entry: Dashboard Home Screen → Insurance Icon → Insurance Dashboard Activity
    ├── Load → GET /v4/insurance → Display Insurance List, History, Banners, Testimonials
    ├── Select Insurance (Internal) → Check Resume Journey → Show Popup or Navigate to Purchase Flow
    ├── Select Insurance (External) → Navigate to Insurance Lead Generation Activity
    ├── Resume Journey (Continue) → Navigate via Deep Link
    ├── Resume Journey (Restart) → PUT /v3/insurance/purchase/restart → Navigate to Purchase Flow
    ├── My Policies → Navigate to User Policies Activity
    ├── Wallet → Navigate to Wallet Activity
    ├── Vault → Navigate to Vault Screen (Deep Link)
    ├── Employee Benefits → Navigate to Employee Benefits Detail Activity
    ├── Call Now → Request Phone Permission → Dial Support Number
    ├── Chat (Messenger) → Open Messenger Link
    ├── Support Chat (Intercom) → Open Intercom Chat
    ├── Purchase Completed → Finish Activity → Return to Previous Screen
    ├── Purchase Cancelled → Refresh Insurance List
    └── Back → Navigate Back (if task root, navigate to Dashboard)
```

---

## Business Logic

### Insurance Selection Flow
1. User clicks on insurance category
2. Check `resourceType`:
   - If "EXTERNAL" → Navigate to Lead Generation Activity with URL
   - If "INTERNAL" → Continue to step 3
3. Check `resumeInsurancePurchase.canResumeJourney`:
   - If `true` → Show resume popup with continue/restart options
   - If `false` → Navigate directly to purchase flow
4. Purchase flow navigation:
   - If Cardio Insurance → Navigate to Cardio Insurance Details Activity
   - If other insurance → Navigate to Insurance Profile Confirmation Activity

### Resume Purchase Journey
- Global resume data: From `data.resumeInsurancePurchase` (applies to any category)
- Category-specific resume data: From each category's `resumeInsurancePurchase` object
- When user selects insurance:
  - Check category-specific resume data first
  - If available, show resume popup
  - User can continue from deep link or restart journey

### Restart Journey Flow
- When user chooses "Restart":
  - API call to restart journey
  - On success: Clear saved resume data
  - Navigate to purchase flow (Cardio or Profile Confirmation)
- When user chooses "Continue":
  - Navigate using `resumeScreenDeepLink`
  - No API call needed

### Purchase Result Handling
- If purchase completed (`RESULT_OK`):
  - Activity finishes
  - User returns to previous screen
- If purchase cancelled (`RESULT_CANCELED`):
  - Refresh insurance list
  - Show shimmer effect during refresh
  - Updated data displayed

### My Policies Section
- Visibility based on `historyList`:
  - If `historyList` is not empty → Section visible
  - If `historyList` is empty → Section hidden

### Banners and Testimonials
- Displayed in horizontal scrollable lists
- Pagination indicators shown
- If lists are empty → Sections hidden

